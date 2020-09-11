from edc_visit_schedule import FormsCollection, Crf

crf = {}

potlako_crfs_prn = FormsCollection(
    Crf(show_order=1, model='potlako_subject.missedcall',
        required=False, additional=False),
    Crf(show_order=2, model='potlako_subject.homevisit',
        required=False, additional=False),
    Crf(show_order=3, model='potlako_subject.sms',
        required=False, additional=False),
    name='potlako_crf_prn')

crfs_initial = FormsCollection(
    Crf(show_order=1, model='potlako_subject.patientcallinitial'),
    Crf(show_order=2, model='potlako_subject.symptomandcareseekingassessment'),
    Crf(show_order=3, model='potlako_subject.transport', required=False),
    Crf(show_order=4, model='potlako_subject.physicianreview', required=False),
    Crf(show_order=5, model='potlako_subject.investigationsordered', required=False),
    Crf(show_order=6, model='potlako_subject.investigationsresulted', required=False),
    Crf(show_order=7, model='potlako_subject.medicaldiagnosis', required=False),
    name='initial',
)

crfs_unscheduled = FormsCollection(
    Crf(show_order=1, model='potlako_subject.patientcallfollowup',),
    Crf(show_order=2, model='potlako_subject.cancerdxandtx',),
    Crf(show_order=3, model='potlako_subject.transport', required=False),
    Crf(show_order=4, model='potlako_subject.missedvisit', required=False),
    Crf(show_order=5, model='potlako_subject.investigationsordered', required=False),
    Crf(show_order=6, model='potlako_subject.investigationsresulted', required=False),
    name='post_unscheduled',
)

crfs_followup = FormsCollection(
    Crf(show_order=1, model='potlako_subject.patientcallfollowup'),
    Crf(show_order=2, model='potlako_subject.cancerdxandtx'),
    Crf(show_order=3, model='potlako_subject.transport', required=False),
    Crf(show_order=4, model='potlako_subject.investigationsordered', required=False),
    Crf(show_order=5, model='potlako_subject.investigationsresulted', required=False),
    Crf(show_order=6, model='potlako_subject.missedvisit', required=False),
    name='followup',
)

crf.update({'initial': crfs_initial,
            'followup': crfs_followup,
            'unscheduled': crfs_unscheduled,
            'prn': potlako_crfs_prn})
