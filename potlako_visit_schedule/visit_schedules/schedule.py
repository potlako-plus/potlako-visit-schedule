from dateutil.relativedelta import relativedelta
from edc_visit_schedule import Schedule, Visit

from .crfs import crf
from .requisitions import requisitions

# schedule for new participants
schedule1 = Schedule(
    name='schedule',
    verbose_name='Potlako',
    onschedule_model='potlako_subject.onschedule',
    offschedule_model='potlako_prn.subjectoffstudy',
    consent_model='potlako_subject.subjectconsent',
    appointment_model='edc_appointment.appointment')

visit0 = Visit(
    code='1000',
    title='Enrollment Visit',
    timepoint=0,
    rbase=relativedelta(days=0),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    requisitions=requisitions,
    crfs=crf.get(1000),
    facility_name='5-day clinic')

visit1 = Visit(
    code='1300',
    title='Follow-up Visit 3 months',
    timepoint=1,
    rbase=relativedelta(months=3),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    requisitions=requisitions,
    crfs=crf.get(1300),
    facility_name='5-day clinic')

visit2 = Visit(
    code='1600',
    title='Follow-up Visit 6 months',
    timepoint=2,
    rbase=relativedelta(months=6),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    requisitions=requisitions,
    crfs=crf.get(1600),
    facility_name='5-day clinic')

visit3 = Visit(
    code='1900',
    title='Follow-up Visit 9 months',
    timepoint=3,
    rbase=relativedelta(months=9),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    requisitions=requisitions,
    crfs=crf.get(1900),
    facility_name='5-day clinic')

visit4 = Visit(
    code='2200',
    title='Follow-up Visit 12 months',
    timepoint=4,
    rbase=relativedelta(months=12),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    requisitions=requisitions,
    crfs=crf.get(2200),
    facility_name='5-day clinic')

visit5 = Visit(
    code='2500',
    title='Follow-up Visit 15 months',
    timepoint=5,
    rbase=relativedelta(months=15),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    requisitions=requisitions,
    crfs=crf.get(2500),
    facility_name='5-day clinic')

visit6 = Visit(
    code='2800',
    title='Follow-up Visit 18 months',
    timepoint=6,
    rbase=relativedelta(months=18),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    requisitions=requisitions,
    crfs=crf.get(2800),
    facility_name='5-day clinic')

visit7 = Visit(
    code='3100',
    title='Follow-up Visit 21 months',
    timepoint=7,
    rbase=relativedelta(months=21),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    requisitions=requisitions,
    crfs=crf.get(3100),
    facility_name='5-day clinic')

visit8 = Visit(
    code='3400',
    title='Follow-up Visit 24 months',
    timepoint=8,
    rbase=relativedelta(months=24),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    requisitions=requisitions,
    crfs=crf.get(3400),
    facility_name='5-day clinic')

visit9 = Visit(
    code='3700',
    title='Follow-up Visit 27 months',
    timepoint=9,
    rbase=relativedelta(months=27),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    requisitions=requisitions,
    crfs=crf.get(3700),
    facility_name='5-day clinic')

visit10 = Visit(
    code='4000',
    title='Follow-up Visit 30 months',
    timepoint=10,
    rbase=relativedelta(months=30),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    requisitions=requisitions,
    crfs=crf.get(4000),
    facility_name='5-day clinic')

visit11 = Visit(
    code='4300',
    title='Follow-up Visit 33 months',
    timepoint=11,
    rbase=relativedelta(months=33),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    requisitions=requisitions,
    crfs=crf.get(4300),
    facility_name='5-day clinic')

visit12 = Visit(
    code='4600',
    title='Follow-up Visit 36 months',
    timepoint=12,
    rbase=relativedelta(months=36),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    requisitions=requisitions,
    crfs=crf.get(4600),
    facility_name='5-day clinic')

visit13 = Visit(
    code='4900',
    title='Follow-up Visit 39 months',
    timepoint=13,
    rbase=relativedelta(months=39),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    requisitions=requisitions,
    crfs=crf.get(4900),
    facility_name='5-day clinic')

#
visit14 = Visit(
    code='5200',
    title='Follow-up Visit 42 months',
    timepoint=14,
    rbase=relativedelta(months=42),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    requisitions=requisitions,
    crfs=crf.get(5200),
    facility_name='5-day clinic')

visit15 = Visit(
    code='5500',
    title='Follow-up Visit 45 months',
    timepoint=15,
    rbase=relativedelta(months=45),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    requisitions=requisitions,
    crfs=crf.get(5500),
    facility_name='5-day clinic')

visit16 = Visit(
    code='5800',
    title='Follow-up Visit 48 months',
    timepoint=16,
    rbase=relativedelta(months=48),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    requisitions=requisitions,
    crfs=crf.get(5800),
    facility_name='5-day clinic')

visit17 = Visit(
    code='6100',
    title='Follow-up Visit 51 months',
    timepoint=17,
    rbase=relativedelta(months=51),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    requisitions=requisitions,
    crfs=crf.get(6100),
    facility_name='5-day clinic')

visit18 = Visit(
    code='6400',
    title='Follow-up Visit 54 months',
    timepoint=18,
    rbase=relativedelta(months=54),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    requisitions=requisitions,
    crfs=crf.get(6400),
    facility_name='5-day clinic')

visit19 = Visit(
    code='6700',
    title='Follow-up Visit 57 months',
    timepoint=19,
    rbase=relativedelta(months=57),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    requisitions=requisitions,
    crfs=crf.get(6700),
    facility_name='5-day clinic')

visit20 = Visit(
    code='7000',
    title='Follow-up Visit 60 months',
    timepoint=20,
    rbase=relativedelta(months=60),
    rlower=relativedelta(days=0),
    rupper=relativedelta(days=0),
    requisitions=requisitions,
    crfs=crf.get(7000),
    facility_name='5-day clinic')

schedule1.add_visit(visit=visit0)
schedule1.add_visit(visit=visit1)
schedule1.add_visit(visit=visit2)
schedule1.add_visit(visit=visit3)
schedule1.add_visit(visit=visit4)
schedule1.add_visit(visit=visit5)
schedule1.add_visit(visit=visit6)
schedule1.add_visit(visit=visit7)
schedule1.add_visit(visit=visit8)
schedule1.add_visit(visit=visit9)
schedule1.add_visit(visit=visit10)
schedule1.add_visit(visit=visit11)
schedule1.add_visit(visit=visit12)
schedule1.add_visit(visit=visit13)
schedule1.add_visit(visit=visit14)
schedule1.add_visit(visit=visit15)
schedule1.add_visit(visit=visit16)
schedule1.add_visit(visit=visit17)
schedule1.add_visit(visit=visit18)
schedule1.add_visit(visit=visit19)
schedule1.add_visit(visit=visit20)