/* Serious Labs Consulting.
   Le tableau du marché : le curseur, ou le survol d'une barre, change l'année
   affichée ; les chiffres viennent de assets/data/marche.json, tiré des
   données ouvertes de l'ANJ par outils/marche.py. Puis l'envoi du formulaire.
   Sans script, le tableau montre 2024 et sa table de données ; le formulaire
   reste caché, parce que le serveur écarte tout envoi sans l'horodatage que
   pose ce script. */
(() => {
  const en = document.documentElement.lang === 'en';

  /* ------------------------------------------------------- le tableau -- */

  const board = document.querySelector('[data-board]');
  if (board) {
    const scrub = board.querySelector('[data-scrub]');
    const yearOut = board.querySelector('[data-year]');
    const readout = board.querySelector('[data-readout]');
    const plot = board.querySelector('[data-chart]');
    const bars = [...board.querySelectorAll('.chart__bar')];
    const years = [...board.querySelectorAll('.chart__years li')];
    const fig = (k) => board.querySelector(`[data-fig="${k}"]`);

    const loc = en ? 'en-GB' : 'fr-FR';
    const dec = (v, n) => v.toLocaleString(loc, { minimumFractionDigits: n, maximumFractionDigits: n });
    // Montants en millions d'euros, comptes en milliers : l'unité du fichier.
    const eur = (m) => m >= 1000
      ? (en ? `€${dec(m / 1000, 2)}bn` : `${dec(m / 1000, 2)} Md€`)
      : (en ? `€${dec(m, 0)}m` : `${dec(m, 0)} M€`);
    // En grand, « M » ; « millions » en toutes lettres ferait passer le chiffre
    // sur deux lignes. La ligne d'appoint, elle, l'écrit.
    const mio = (k) => en ? `${dec(k / 1000, 2)}M` : `${dec(k / 1000, 2)} M`;
    const mioLong = (k) => en ? `${dec(k / 1000, 2)}M` : `${dec(k / 1000, 2)} millions`;

    const live = board.querySelector('[data-live]');
    let d = null;
    let sel = bars.length - 1;
    let touched = false;

    // L'année choisie est marquée sous sa barre, en encre ; l'année survolée
    // l'est plus légèrement. Aucune barre n'est atténuée : l'historique reste
    // lisible.
    const mark = (hover) => {
      years.forEach((li, j) => {
        li.classList.toggle('is-sel', j === sel);
        li.classList.toggle('is-hover', j === hover && j !== sel);
        // Les millésimes voisins s'effacent pour ne pas chevaucher le choisi.
        li.classList.toggle('is-near', Math.abs(j - sel) === 1 || (hover != null && Math.abs(j - hover) === 1));
      });
      bars.forEach((b, j) => b.classList.toggle('is-hover', j === hover));
    };

    const show = (i) => {
      const pbj = d.pbj_ps[i] + d.pbj_po[i] + d.pbj_ph[i];
      const an = d.annees[i] + (d.annees[i] === 2010 ? '*' : '');
      yearOut.textContent = an;
      fig('pbj').textContent = eur(pbj);
      fig('comptes').textContent = mio(d.comptes[i]);
      fig('uniques').textContent = d.uniques[i] == null
        ? (en ? 'Unique players not published' : 'Joueurs uniques non publiés')
        : (en ? `${mioLong(d.uniques[i])} unique players` : `${mioLong(d.uniques[i])} de joueurs uniques`);
      fig('operateurs').textContent = d.operateurs[i];
      fig('agrements').textContent = en ? `${d.agrements[i]} licences` : `${d.agrements[i]} agréments`;
      fig('mises').textContent = eur(d.mises_ps[i] + d.mises_ph[i]);
      readout.textContent = en
        ? `${an}: sports betting ${eur(d.pbj_ps[i])} · poker ${eur(d.pbj_po[i])} · horse racing ${eur(d.pbj_ph[i])}`
        : `${an} : paris sportifs ${eur(d.pbj_ps[i])} · poker ${eur(d.pbj_po[i])} · paris hippiques ${eur(d.pbj_ph[i])}`;
    };

    // Le lecteur d'écran n'entend que les choix (curseur, clic), pas les
    // survols, et rien au chargement.
    const select = (i) => {
      sel = i;
      scrub.value = d.annees[i];
      show(i);
      mark();
      if (touched) live.textContent = readout.textContent;
      touched = true;
    };

    fetch('/assets/data/marche.json')
      .then((r) => r.json())
      .then((data) => {
        d = data;
        bars.forEach((bar, i) => {
          bar.addEventListener('pointerenter', (e) => {
            if (e.pointerType !== 'mouse') return;
            mark(i);
            show(i);
          });
          // Au toucher comme à la souris, un clic choisit l'année.
          bar.addEventListener('click', () => select(i));
        });
        plot.addEventListener('pointerleave', (e) => {
          if (e.pointerType !== 'mouse') return;
          mark();
          show(sel);
        });
        scrub.addEventListener('input', () => select(d.annees.indexOf(Number(scrub.value))));
        board.classList.add('is-live');
        select(sel);
      })
      .catch(() => {});
  }

  /* ----------------------------------------------------- le formulaire -- */

  const form = document.querySelector('[data-contact-form]');
  if (!form) return;

  form.hidden = false;
  const status = form.querySelector('[data-status]');
  const submit = form.querySelector('[type="submit"]');
  const submitLabel = submit.textContent;
  const msg = {
    sending: en ? 'Sending…' : 'Envoi en cours…',
    ok: en ? 'Received. Antoine Dugast will reply personally.' : 'Reçu. Antoine Dugast vous répondra personnellement.',
    ko: en ? 'The message could not be sent. Please try again in a moment.'
           : "Le message n'a pas pu partir. Réessayez dans un instant.",
    invalid: en ? 'The form is not complete: see the messages under the fields.'
                : 'Le formulaire est incomplet : voyez les messages sous les champs.',
  };
  const why = (el) => {
    if (el.type === 'checkbox') return en ? 'Tick this box so we can answer you.' : 'Cochez cette case pour que nous puissions vous répondre.';
    if (el.validity.typeMismatch) return en ? 'This email address looks incomplete.' : 'Cette adresse de courriel semble incomplète.';
    return en ? 'This field is required.' : 'Ce champ est obligatoire.';
  };

  const say = (kind, text) => {
    status.hidden = false;
    status.className = `reply f--wide reply--${kind}`;
    status.textContent = text;
  };

  // Le formulaire porte novalidate et l'envoi est intercepté : sans ce
  // contrôle, un champ manquant ne serait signalé à personne.
  const markInvalid = () => {
    form.querySelectorAll('[aria-invalid]').forEach((el) => { el.removeAttribute('aria-invalid'); el.removeAttribute('aria-describedby'); });
    form.querySelectorAll('.f__err').forEach((p) => p.remove());
    const bad = [...form.querySelectorAll('input:invalid, textarea:invalid')];
    for (const el of bad) {
      const err = document.createElement('p');
      err.className = el.type === 'checkbox' ? 'f__err f--wide' : 'f__err';
      err.id = `err-${el.name}`;
      err.textContent = why(el);
      (el.type === 'checkbox' ? el.closest('label') : el).after(err);
      el.setAttribute('aria-invalid', 'true');
      el.setAttribute('aria-describedby', err.id);
    }
    bad[0]?.focus();
    return bad.length;
  };

  // Une erreur s'efface dès que le champ est corrigé.
  form.addEventListener('input', (e) => {
    const el = e.target;
    if (el.getAttribute('aria-invalid') !== 'true' || !el.checkValidity()) return;
    document.getElementById(el.getAttribute('aria-describedby'))?.remove();
    el.removeAttribute('aria-invalid');
    el.removeAttribute('aria-describedby');
  });

  // Horodatage posé par le navigateur : le serveur refuse les envois trop
  // rapides et ceux qui arrivent sans lui.
  form.querySelector('[name="ts"]').value = String(Math.round(performance.timeOrigin + performance.now()));

  form.addEventListener('submit', (ev) => {
    ev.preventDefault();
    if (markInvalid()) { say('ko', msg.invalid); return; }

    say('ok', msg.sending);
    submit.disabled = true;
    submit.textContent = msg.sending;

    fetch(form.action, { method: 'POST', body: new FormData(form) })
      .then((r) => r.json().then((data) => ({ ok: r.ok, data })))
      .then((res) => {
        if (res.ok && res.data?.ok) {
          form.reset();
          say('ok', msg.ok);
          submit.remove();
          return;
        }
        say('ko', res.data?.error || msg.ko);
        submit.disabled = false;
        submit.textContent = submitLabel;
      })
      .catch(() => {
        say('ko', msg.ko);
        submit.disabled = false;
        submit.textContent = submitLabel;
      });
  });
})();
