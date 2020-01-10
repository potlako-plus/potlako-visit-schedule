from edc_visit_schedule import FormsCollection, Crf

crf = {}

crfs_1000 = FormsCollection(
    Crf(show_order=1, model='potlako_subject.cliniciancallenrollment'),
    Crf(show_order=2, model='potlako_subject.cliniciancallfollowup'),
    Crf(show_order=3, model='potlako_subject.patientcallinitial'),
    Crf(show_order=4, model='potlako_subject.patientcallfollowup'),
    Crf(show_order=5, model='potlako_subject.missedvisit'),
    Crf(show_order=6, model='potlako_subject.transport'),
    Crf(show_order=7, model='potlako_subject.homevisit'),
    Crf(show_order=8, model='potlako_subject.physicianreview'),
    Crf(show_order=9, model='potlako_subject.patientstatus'),
    Crf(show_order=10, model='potlako_subject.missedcall'),
    name='initial',
    )

crf.update({1000: crfs_1000})
