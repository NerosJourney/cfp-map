import db
import scraper

conference_list = scraper.get_conferences('robotics')
for conference in conference_list:
    print(conference)
    db.add_conference_safely(conference)