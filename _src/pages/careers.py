"""Careers — footer page. Italian uses the informal "tu" here (and only here)."""


def render(c):
    t, I = c.t, c.icon

    values = [
        (t('Structured GVP training', 'Formazione GVP strutturata'),
         t('Each role has a training plan, with documented steps from first case to independent work.',
           'Ogni ruolo ha un piano di formazione, con tappe documentate dal primo caso al lavoro in autonomia.')),
        (t('A defined competency path', 'Un percorso di competenze definito'),
         t('You know what is expected at each level, from data entry to senior drug safety officer.',
           'Sai cosa è richiesto a ogni livello, dal data entry al drug safety officer senior.')),
        (t('Work that matters', 'Un lavoro che conta'),
         t('Every case you handle contributes to the safe use of medicines.',
           'Ogni caso che gestisci contribuisce all\'uso sicuro dei medicinali.')),
    ]
    vals = "".join(f"""
          <div class="point reveal">
            <h3 class="point__title">{a}</h3>
            <p class="point__text">{b}</p>
          </div>""" for a, b in values)

    profiles = [
        (t('Quality Assurance, pharmacovigilance', 'Quality Assurance di farmacovigilanza'),
         t('5+ years of experience.', 'Almeno 5 anni di esperienza.')),
        (t('Medical Expert', 'Medical Expert'),
         t('Degree in medicine, 2+ years of experience.', 'Laurea in medicina, almeno 2 anni di esperienza.')),
        (t('Drug Safety Officer, senior and junior', 'Drug Safety Officer, senior e junior'), ''),
        (t('Data Entry Operator', 'Data Entry Operator'), ''),
    ]
    prof = "".join(f"""
          <div class="point point--draft reveal">
            <h3 class="point__title">{a}</h3>
            {f'<p class="point__text">{b}</p>' if b else ''}
          </div>""" for a, b in profiles)

    body = c.page_header(
        t('Careers', 'Lavora con noi'),
        t('Work in pharmacovigilance, with a team that trains you', 'Lavora nella farmacovigilanza, con un team che ti forma'),
        t('We look for physicians, pharmacists, biologists and quality professionals who want to grow in drug safety.',
          'Cerchiamo medici, farmacisti, biologi e professionisti della qualità che vogliono crescere nella drug safety.'),
    ) + f"""

  <section class="section" aria-labelledby="why-mac">
    <div class="container">
      <span class="section-label section-label--primary reveal">{t('Working at MAC', 'Lavorare in MAC')}</span>
      <h2 class="reveal reveal-delay-1" id="why-mac">{t('How you grow here', 'Come cresci qui')}</h2>
      <div class="section-divider reveal reveal-delay-2"></div>
      <div class="point-grid point-grid--3">{vals}
      </div>
    </div>
  </section>

  <section class="section section--bg" aria-labelledby="profiles">
    <div class="container">
      <span class="section-label section-label--primary reveal">{t('Profiles', 'Profili')}</span>
      <h2 class="reveal reveal-delay-1" id="profiles">{t('The roles on our team', 'I ruoli del nostro team')}</h2>
      <div class="section-divider reveal reveal-delay-2"></div>
      <p class="section-note reveal">{c.draft('profili e requisiti da completare sulla slide 5 della company presentation')}</p>
      <div class="point-grid point-grid--2">{prof}
      </div>
    </div>
  </section>

  <section class="section" id="apply" aria-labelledby="apply-title">
    <div class="container" style="max-width:760px;text-align:center;">
      <span class="section-label section-label--primary reveal">{t('Apply', 'Candidati')}</span>
      <h2 class="reveal reveal-delay-1" id="apply-title">{t('Send us your CV', 'Inviaci il tuo CV')}</h2>
      <p class="reveal reveal-delay-2" style="margin:1rem auto 2rem;">{t(
          'There are no open positions at the moment. We read every application and get in touch when a suitable role opens.',
          'Al momento non ci sono posizioni aperte. Leggiamo tutte le candidature e ti contattiamo quando si apre un ruolo adatto.')}</p>
      <a href="mailto:recruiting@med-af-consulting.it" class="btn btn--primary btn--lg reveal reveal-delay-2">{I['mail']} recruiting@med-af-consulting.it</a>
      <p class="contact-note reveal reveal-delay-3">{t('Attach your CV as a PDF. We handle your data as described in the',
                                                       'Allega il CV in PDF. Trattiamo i tuoi dati come descritto nell\'')}
        <a href="{c.url('privacy-candidates')}">{t('privacy notice for candidates', 'informativa privacy per i candidati')}</a>.</p>
    </div>
  </section>
{c.cta(t('Curious about who you would work with?', 'Vuoi sapere con chi lavoreresti?'),
       t('Meet the team', 'Conosci il team'), href=c.url('about'))}"""

    return {
        "title": t("Careers in pharmacovigilance · MAC", "Lavorare nella farmacovigilanza · MAC"),
        "desc": t("Roles, training and how to apply to Medical Affairs Consulting, a pharmacovigilance team in Saronno, near Milan.",
                  "Ruoli, formazione e come candidarsi a Medical Affairs Consulting, un team di farmacovigilanza a Saronno, vicino a Milano."),
        "body": body,
    }
