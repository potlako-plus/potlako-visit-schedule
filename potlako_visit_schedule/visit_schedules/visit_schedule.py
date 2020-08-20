from edc_visit_schedule import VisitSchedule, site_visit_schedules

from .schedule import potlako_plus_schedule

potlako_visit_schedule = VisitSchedule(
    name='potlako_visit_schedule',
    verbose_name='potlako_plus',
    offstudy_model='potlako_prn.subjectoffstudy',
    locator_model='potlako_subject.subjectlocator',
    death_report_model='potlako_prn.deathreport',
    previous_visit_schedule=None)

potlako_visit_schedule.add_schedule(potlako_plus_schedule)

site_visit_schedules.register(potlako_visit_schedule)
