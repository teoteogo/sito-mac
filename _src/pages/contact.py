"""Contact — section 5.6 of the copy document."""
from urllib.parse import quote

import build


def render(c):
    t, I = c.t, c.icon

    items = [
        t('Products and countries', 'Prodotti e paesi'),
        t('Case volumes per year', 'Volumi annui di casi'),
        t('Services you are considering', 'Servizi che state valutando'),
        t('Upcoming deadlines, such as an inspection, a PSUR or a change of QPPV',
          'Scadenze in arrivo, per esempio un\'ispezione, uno PSUR o un cambio di QPPV'),
    ]
    subject = t('Pharmacovigilance enquiry', 'Richiesta farmacovigilanza')
    mail_body = "\n".join(f"{x}:\n" for x in [
        t('Products and countries', 'Prodotti e paesi'),
        t('Case volumes per year', 'Volumi annui di casi'),
        t('Services we are considering', 'Servizi che stiamo valutando'),
        t('Upcoming deadlines', 'Scadenze in arrivo'),
    ])
    mailto = f"mailto:{build.EMAIL}?subject={quote(subject)}&amp;body={quote(mail_body)}"

    body = c.page_header(
        t('Contact', 'Contatti'),
        t('Tell us what you need to cover', 'Diteci cosa dovete coprire'),
        t('Write to us. We reply within one working day, and your message goes straight to the pharmacovigilance team.',
          'Scriveteci. Rispondiamo entro un giorno lavorativo, e il vostro messaggio arriva direttamente al team di farmacovigilanza.'),
    ) + f"""

  <section class="section">
    <div class="container">
      <div class="contact-layout">

        <div class="contact-form-col">
          <span class="section-label section-label--primary reveal">{t('Your first message', 'Il primo messaggio')}</span>
          <h2 class="reveal reveal-delay-1">{t('What to include', 'Cosa indicarci')}</h2>
          <ul class="tick-list reveal reveal-delay-2">
            {''.join(f'<li>{I["check"]}<span>{x}</span></li>' for x in items)}
          </ul>
          <div class="reveal reveal-delay-2" style="margin-top:2rem;">
            <a href="{mailto}" class="btn btn--primary btn--lg">{I['mail']} {t('Write to us', 'Scriveteci')}</a>
            <p class="contact-email">{t('or write to', 'oppure scrivete a')} <a href="mailto:{build.EMAIL}">{build.EMAIL}</a></p>
            <p class="contact-note">{t('Before writing, please read how we handle your data.', 'Prima di scriverci, leggete come trattiamo i vostri dati.')}
              <a href="{c.url('privacy-clients')}">{t('Privacy notice', 'Informativa privacy')}</a></p>
          </div>
          <p class="contact-warning reveal reveal-delay-3" role="note">{t(
              'Please do not send patient data or adverse reaction reports to this address.',
              'Non inviate a questo indirizzo dati di pazienti o segnalazioni di reazioni avverse.')}</p>
        </div>

        <div class="contact-info-col">
          <span class="section-label section-label--primary reveal">{t('Where to find us', 'Dove siamo')}</span>
          <h2 class="reveal reveal-delay-1">{t('Contact details', 'Recapiti')}</h2>

          <hr class="contact-info-divider">
          <div class="contact-info-item reveal reveal-delay-2">
            <span class="contact-info-label">Email</span>
            <span class="contact-info-detail"><a href="mailto:{build.EMAIL}">{build.EMAIL}</a></span>
          </div>

          <hr class="contact-info-divider">
          <div class="contact-info-item reveal reveal-delay-3">
            <span class="contact-info-label">{t('Telephone', 'Telefono')}</span>
            <span class="contact-info-detail">{c.draft('numero di centralino')}</span>
          </div>

          <hr class="contact-info-divider">
          <div class="contact-info-item reveal reveal-delay-4">
            <span class="contact-info-label">{t('Address', 'Indirizzo')}</span>
            <address class="contact-info-detail" style="font-style:normal;">
              Medical Affairs Consulting S.r.l.<br>Corso Italia 39<br>21047 Saronno (VA){t(', Italy', '')}
            </address>
          </div>

          <hr class="contact-info-divider">
          <div class="contact-info-item reveal reveal-delay-5">
            <span class="contact-info-label">LinkedIn</span>
            <span class="contact-info-detail"><a href="{build.LINKEDIN}" target="_blank" rel="noopener">Medical Affairs Consulting</a></span>
          </div>
        </div>

      </div>
    </div>
  </section>"""

    return {
        "title": t("Contact the pharmacovigilance team · MAC", "Contattate il team di farmacovigilanza · MAC"),
        "desc": t("Tell us which products, countries and case volumes you need to cover. We reply within one working day.",
                  "Diteci quali prodotti, paesi e volumi di casi dovete coprire. Rispondiamo entro un giorno lavorativo."),
        "body": body,
    }
