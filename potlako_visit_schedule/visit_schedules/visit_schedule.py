from edc_visit_schedule import VisitSchedule, site_visit_schedules

from .schedules import intervention_schedule, enhanced_care_schedule

intervention_visit_schedule = VisitSchedule(
    name='intervention_visit_schedule',
    verbose_name='potlako',
    offstudy_model='potlako_prn.subjectoffstudy',
    locator_model='potlako_subject.subjectlocator',
    death_report_model='potlako_prn.deathreport',
    previous_visit_schedule=None)

intervention_visit_schedule.add_schedule(intervention_schedule)

enhanced_care_visit_schedule = VisitSchedule(
    name='enhanced_care_visit_schedule',
    verbose_name='potlako',
    offstudy_model='potlako_prn.subjectoffstudy',
    locator_model='potlako_subject.subjectlocator',
    death_report_model='potlako_prn.deathreport',
    previous_visit_schedule=None)

enhanced_care_visit_schedule.add_schedule(enhanced_care_schedule)

site_visit_schedules.register(enhanced_care_visit_schedule)
site_visit_schedules.register(intervention_visit_schedule)
