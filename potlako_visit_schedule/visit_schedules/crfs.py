from edc_visit_schedule import FormsCollection, Crf

crf = {}

crfs_prn = FormsCollection(
    Crf(show_order=1, model='potlako_subject.cliniciancallfollowup',
        required=False, additional=False),
    name='potlako_crf_prn')

crfs_1000 = FormsCollection(
    Crf(show_order=1, model='potlako_subject.patientcallinitial'),
    Crf(show_order=4, model='potlako_subject.transport', required=False),
    Crf(show_order=5, model='potlako_subject.homevisit', required=False),
    Crf(show_order=6, model='potlako_subject.physicianreview', required=False),
    name='initial',
)

crfs_unscheduled = FormsCollection(
    Crf(show_order=1, model='potlako_subject.patientcallfollowup'),
    Crf(show_order=4, model='potlako_subject.transport', required=False),
    Crf(show_order=5, model='potlako_subject.homevisit', required=False),
    Crf(show_order=6, model='potlako_subject.physicianreview', required=False),
    name='unscheduled',
)

# crfs_offstudy = FormsCollection(
#     Crf(show_order=1, model='potlako_subject.patientcallfollowup'),
#     Crf(show_order=4, model='potlako_subject.transport', required=False),
#     Crf(show_order=5, model='potlako_subject.homevisit', required=False),
#     Crf(show_order=6, model='potlako_subject.physicianreview', required=False),
#     name='offstudy_crfs',
# )

crf.update({'initial': crfs_1000,
            'unscheduled': crfs_unscheduled,
            'prn': crfs_prn})
