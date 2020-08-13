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
enhanced_care_schedule = Schedule(
    name='enhanced_care_schedule',
    verbose_name='Potlako+',
    onschedule_model='potlako_subject.onscheduleenhancedcare',
    offschedule_model='potlako_prn.subjectoffstudy',
    consent_model='potlako_subject.subjectconsent',
    appointment_model='edc_appointment.appointment')

visit0 = Visit(
    code='1000',
    title='Enhanced Care Visit 1',
    timepoint=0,
    rbase=relativedelta(days=0),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    requisitions=requisitions,
    crfs=crf.get('initial'),
    facility_name='5-day clinic')

visit1 = Visit(
    code='2000',
    title='Enhanced Care Visit 2',
    timepoint=1,
    rbase=relativedelta(months=6),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    requisitions=requisitions,
    crfs=crf.get('followup'),
    facility_name='5-day clinic')

visit2 = Visit(
    code='3000',
    title='Enhanced Care Visit 3',
    timepoint=2,
    rbase=relativedelta(months=12),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    requisitions=requisitions,
    crfs=crf.get('followup'),
    facility_name='5-day clinic')

enhanced_care_schedule.add_visit(visit=visit0)
enhanced_care_schedule.add_visit(visit=visit1)
enhanced_care_schedule.add_visit(visit=visit2)
