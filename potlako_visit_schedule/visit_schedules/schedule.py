from dateutil.relativedelta import relativedelta
from edc_visit_schedule import Schedule, Visit as BaseVisit

from .crfs import crf, potlako_crfs_prn
from .requisitions import requisitions


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
potlako_plus_schedule = Schedule(
    name='potlako_plus_schedule',
    verbose_name='Potlako+',
    onschedule_model='potlako_subject.onschedule',
    offschedule_model='potlako_prn.subjectoffstudy',
    consent_model='potlako_subject.subjectconsent',
    appointment_model='edc_appointment.appointment')

visit0 = Visit(
    code='1000',
    title='Initial Visit',
    timepoint=0,
    rbase=relativedelta(days=0),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    requisitions=requisitions,
    crfs=crf.get('initial'),
    facility_name='5-day clinic')

visit1 = Visit(
    code='2000',
    title='6 months visit',
    timepoint=2,
    rbase=relativedelta(months=6),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    requisitions=requisitions,
    crfs=crf.get('followup'),
    facility_name='5-day clinic')

visit2 = Visit(
    code='3000',
    title='12 months visit',
    timepoint=4,
    rbase=relativedelta(months=12),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    requisitions=requisitions,
    crfs=crf.get('followup'),
    facility_name='5-day clinic')

potlako_plus_schedule.add_visit(visit=visit0)
potlako_plus_schedule.add_visit(visit=visit1)
potlako_plus_schedule.add_visit(visit=visit2)
