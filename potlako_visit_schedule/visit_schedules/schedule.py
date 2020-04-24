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
schedule1 = Schedule(
    name='schedule',
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
    code='1010',
    title='Followup Visit',
    timepoint=1,
    rbase=relativedelta(days=10),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    requisitions=requisitions,
    crfs=crf.get('unscheduled'),
    facility_name='5-day clinic')

schedule1.add_visit(visit=visit0)
schedule1.add_visit(visit=visit1)
