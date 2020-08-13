from dateutil.relativedelta import relativedelta
from edc_visit_schedule import Schedule, Visit as BaseVisit

from ..crfs import crf, potlako_crfs_prn
from ..requisitions import requisitions


class Visit(BaseVisit):

    def __init__(self, crfs_unscheduled=None, requisitions_unscheduled=None,
                 crfs_prn=None, requisitions_prn=None,
                 allow_unscheduled=None, **kwargs):
        super().__init__(
            allow_unscheduled=True if allow_unscheduled is None else allow_unscheduled,
            crfs_unscheduled=crf.get('unscheduled') or crfs_unscheduled,
            requisitions_unscheduled=requisitions_unscheduled,
            crfs_prn=potlako_crfs_prn or crfs_prn,
            requisitions_prn=requisitions_prn,
            **kwargs)


# schedule for new participants
intervention_schedule = Schedule(
    name='intervention_schedule',
    verbose_name='Potlako+',
    onschedule_model='potlako_subject.onscheduleintervention',
    offschedule_model='potlako_prn.subjectoffstudy',
    consent_model='potlako_subject.subjectconsent',
    appointment_model='edc_appointment.appointment')

visit0 = Visit(
    code='1000',
    title='Intervention Visit 1',
    timepoint=0,
    rbase=relativedelta(days=0),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    requisitions=requisitions,
    crfs=crf.get('initial'),
    facility_name='5-day clinic')

visit1 = Visit(
    code='1010',
    title='Intervention Visit 2',
    timepoint=1,
    rbase=relativedelta(day=1),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=90),
    requisitions=requisitions,
    crfs=crf.get('post_scheduled'),
    facility_name='5-day clinic')

visit2 = Visit(
    code='2000',
    title='Intervention Visit 3',
    timepoint=2,
    rbase=relativedelta(months=6),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    requisitions=requisitions,
    crfs=crf.get('followup'),
    facility_name='5-day clinic')

visit3 = Visit(
    code='2010',
    title='Intervention Visit 4',
    timepoint=3,
    rbase=relativedelta(months=6, days=2),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=90),
    requisitions=requisitions,
    crfs=crf.get('post_scheduled'),
    facility_name='5-day clinic')

visit4 = Visit(
    code='3000',
    title='Intervention Visit 5',
    timepoint=4,
    rbase=relativedelta(months=12),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    requisitions=requisitions,
    crfs=crf.get('followup'),
    facility_name='5-day clinic')

visit5 = Visit(
    code='3010',
    title='Intervention Visit 6',
    timepoint=5,
    rbase=relativedelta(months=12, days=2),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=90),
    requisitions=requisitions,
    crfs=crf.get('post_scheduled'),
    facility_name='5-day clinic')

intervention_schedule.add_visit(visit=visit0)
intervention_schedule.add_visit(visit=visit1)
intervention_schedule.add_visit(visit=visit2)
intervention_schedule.add_visit(visit=visit3)
intervention_schedule.add_visit(visit=visit4)
intervention_schedule.add_visit(visit=visit5)
