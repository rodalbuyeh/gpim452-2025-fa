#!/usr/bin/env python3

import argparse
import os
from datetime import datetime, timedelta
from typing import List, Dict, Any

class WeekGenerator:
    def __init__(self):
        self.event_types = {
            'LEC': {'label': 'lecture', 'color': 'lecture'},
            'DIS': {'label': 'disc', 'color': 'disc'},
            'LAB': {'label': 'lab', 'color': 'lab'},
            'HW': {'label': 'hw', 'color': 'hw'},
            'QUIZ': {'label': 'quiz', 'color': 'quiz'},
            'EXAM': {'label': 'exam', 'color': 'exam'},
            'PROJ': {'label': 'proj', 'color': 'proj'},
            'SUR': {'label': 'survey', 'color': 'survey'}
        }

    def generate_week(self, week_num: int, title: str, start_date: datetime, events: List[Dict] = None):
        """Generate a week file with the specified parameters."""
        if events is None:
            events = []
            
        content = self._generate_yaml_header(week_num, title)
        content += self._generate_days_section(start_date, events)
        content += "---\n\n"
        
        # Ensure _modules directory exists
        os.makedirs('_modules', exist_ok=True)
        
        filename = f"_modules/week-{week_num:02d}.md"
        
        with open(filename, 'w') as f:
            f.write(content)
        
        print(f"Generated {filename}")
        return filename

    def generate_template(self, week_num: int, title: str, start_date: datetime):
        """Generate a week file with common event structure."""
        events = [
            {
                'date_offset': 0,  # Monday
                'events': [
                    {
                        'type': 'LEC',
                        'number': week_num * 3 - 1,
                        'title': 'Topic Title',
                        'notebook_path': f"lectures/lec{(week_num * 3 - 1):02d}/lec{(week_num * 3 - 1):02d}.ipynb",
                        'reading': '[Reading Reference](link)',
                        'keywords': 'keyword1, keyword2, keyword3'
                    }
                ]
            },
            {
                'date_offset': 2,  # Wednesday
                'events': [
                    {
                        'type': 'LEC',
                        'number': week_num * 3,
                        'title': 'Topic Title',
                        'notebook_path': f"lectures/lec{(week_num * 3):02d}/lec{(week_num * 3):02d}.ipynb",
                        'reading': '[Reading Reference](link)',
                        'keywords': 'keyword1, keyword2, keyword3'
                    },
                    {
                        'type': 'DIS',
                        'number': week_num,
                        'title': 'Discussion Topic',
                        'link': f"https://practice.dsc10.com/disc{week_num:02d}/index.html"
                    }
                ]
            },
            {
                'date_offset': 4,  # Friday
                'events': [
                    {
                        'type': 'LEC',
                        'number': week_num * 3 + 1,
                        'title': 'Topic Title',
                        'notebook_path': f"lectures/lec{(week_num * 3 + 1):02d}/lec{(week_num * 3 + 1):02d}.ipynb",
                        'reading': '[Reading Reference](link)',
                        'keywords': 'keyword1, keyword2, keyword3'
                    }
                ]
            },
            {
                'date_offset': 6,  # Sunday (for homework due)
                'events': [
                    {
                        'type': 'HW',
                        'number': week_num,
                        'title': 'Assignment Title',
                        'notebook_path': f"homeworks/hw{week_num:02d}/hw{week_num:02d}.ipynb"
                    }
                ]
            }
        ]
        
        return self.generate_week(week_num, title, start_date, events)

    def _generate_yaml_header(self, week_num: int, title: str) -> str:
        return f"---\n    title: Week {week_num} – {title}\n    weekNumber: {week_num}\n"

    def _generate_days_section(self, start_date: datetime, events: List[Dict]) -> str:
        content = "    days:\n"
        
        if not events:
            # Generate empty template structure
            for day_offset in range(7):
                date = start_date + timedelta(days=day_offset)
                content += f"      - date: {date.strftime('%Y-%-m-%-d')}\n"
                content += "        events:\n"
                content += "          # Add events here\n"
        else:
            for day_events in events:
                date = start_date + timedelta(days=day_events['date_offset'])
                content += f"      - date: {date.strftime('%Y-%-m-%-d')}\n"
                content += "        events:\n"
                
                for event in day_events['events']:
                    content += self._generate_event(event)
        
        return content

    def _generate_event(self, event: Dict[str, Any]) -> str:
        event_type = event.get('type', 'GENERIC')
        
        if event_type == 'LEC':
            return self._generate_lecture_event(event)
        elif event_type == 'DIS':
            return self._generate_discussion_event(event)
        elif event_type == 'LAB':
            return self._generate_lab_event(event)
        elif event_type == 'HW':
            return self._generate_homework_event(event)
        elif event_type == 'QUIZ':
            return self._generate_quiz_event(event)
        elif event_type == 'EXAM':
            return self._generate_exam_event(event)
        elif event_type == 'PROJ':
            return self._generate_project_event(event)
        elif event_type == 'SUR':
            return self._generate_survey_event(event)
        else:
            return self._generate_generic_event(event)

    def _generate_lecture_event(self, event: Dict[str, Any]) -> str:
        lec_num = f"{event['number']:02d}"
        content = f'          "**LEC {event["number"]}**{{: .label .label-lecture }} [{event["title"]}](http://datahub.ucsd.edu/user-redirect/git-sync?repo=https://github.com/dsc-courses/dsc10-2023-fa&subPath={event["notebook_path"]}) [✏️](resources/lectures/lec{lec_num}/lec{lec_num}.html)":\n'
        
        if event.get('reading'):
            content += f'            "{event["reading"]}"\n'
        
        if event.get('keywords'):
            content += f'          "<small><i><span style=\'display: inline-block; padding-left: 80px\'><b>Keywords:</b> {event["keywords"]}</span></i></small>":\n'
        
        return content

    def _generate_discussion_event(self, event: Dict[str, Any]) -> str:
        return f'          "**DIS {event["number"]}**{{: .label .label-disc }} [{event["title"]}]({event["link"]})":\n'

    def _generate_lab_event(self, event: Dict[str, Any]) -> str:
        return f'          "**Lab {event["number"]}**{{: .label .label-lab }} **[{event["title"]}](http://datahub.ucsd.edu/user-redirect/git-sync?repo=https://github.com/dsc-courses/dsc10-2023-fa&subPath={event["notebook_path"]})**":\n'

    def _generate_homework_event(self, event: Dict[str, Any]) -> str:
        return f'          "**HW {event["number"]}**{{: .label .label-hw }} [**{event["title"]}**](http://datahub.ucsd.edu/user-redirect/git-sync?repo=https://github.com/dsc-courses/dsc10-2023-fa&subPath={event["notebook_path"]})":\n'

    def _generate_quiz_event(self, event: Dict[str, Any]) -> str:
        content = f'          "**QUIZ {event["number"]}**{{: .label .label-quiz }}'
        if event.get('solutions'):
            content += f' [Solutions]({event["solutions"]})'
        content += '":\n'
        return content

    def _generate_exam_event(self, event: Dict[str, Any]) -> str:
        return f'          "**EXAM**{{: .label .label-exam }} **{event["title"]}**":\n'

    def _generate_project_event(self, event: Dict[str, Any]) -> str:
        content = f'          "**PROJ**{{: .label .label-proj }} **[{event["title"]}](http://datahub.ucsd.edu/user-redirect/git-sync?repo=https://github.com/dsc-courses/dsc10-2023-fa&subPath={event["notebook_path"]})**'
        if event.get('partner_guidelines'):
            content += ' (see [partner guidelines](project-partners))'
        content += '":\n'
        return content

    def _generate_survey_event(self, event: Dict[str, Any]) -> str:
        return f'          "**SUR**{{: .label .label-survey }} [**{event["title"]}**]({event["link"]})":\n'

    def _generate_generic_event(self, event: Dict[str, Any]) -> str:
        return f'          "{event["title"]}":\n'


def main():
    parser = argparse.ArgumentParser(description='Generate Jekyll week module files')
    parser.add_argument('week_number', type=int, help='Week number')
    parser.add_argument('title', help='Week title')
    parser.add_argument('start_date', help='Start date (YYYY-MM-DD format)')
    parser.add_argument('--template', action='store_true', 
                       help='Generate with common event structure template')
    
    args = parser.parse_args()
    
    try:
        start_date = datetime.strptime(args.start_date, '%Y-%m-%d')
    except ValueError:
        print("Error: Date must be in YYYY-MM-DD format")
        return 1
    
    generator = WeekGenerator()
    
    if args.template:
        generator.generate_template(args.week_number, args.title, start_date)
    else:
        generator.generate_week(args.week_number, args.title, start_date)
    
    return 0


if __name__ == '__main__':
    exit(main()) 