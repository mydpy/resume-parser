#!/usr/bin/env python3
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfparser import PDFParser
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfdevice import PDFDevice, TagExtractor
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import XMLConverter, HTMLConverter, TextConverter
from pdfminer.cmapdb import CMapDB
from pdfminer.layout import LAParams
from pdfminer.image import ImageWriter
import io


def check_section_start(list_item):
    _list_item = str(list_item)

    if (
            _list_item == "Contact"
            or _list_item == "Top Skills"
            or _list_item == "Certifications"
            or _list_item == "Summary"
            or _list_item == "Languages"
            or _list_item == "Education"
            or _list_item == "Activity"
    ):
        return True
    else:
        return False


def get_contact_index(resume_list):
    start_index = None
    try:
        start_index = resume_list.index("Contact")
    except ValueError as e:
        pass

    return start_index


def get_top_skills_index(resume_list):
    start_index = None
    try:
        start_index = resume_list.index("Top Skills")
    except ValueError as e:
        pass

    try:
        start_index = resume_list.index("Principales compétences")
    except ValueError as e:
        pass

    try:
        start_index = resume_list.index("Top-Kenntnisse")
    except ValueError as e:
        pass

    try:
        start_index = resume_list.index("Främsta kompetenser")
    except ValueError as e:
        pass

    try:
        start_index = resume_list.index("Belangrijkste vaardigheden")
    except ValueError as e:
        pass

    return start_index


def get_languages_index(resume_list):
    start_index = None
    try:
        start_index = resume_list.index("Languages")
    except ValueError as e:
        pass

    return start_index


def get_certifications_index(resume_list):
    start_index = None
    try:
        start_index = resume_list.index("Certifications")
    except ValueError as e:
        pass

    return start_index


def get_honors_awards_index(resume_list):
    start_index = None
    try:
        start_index = resume_list.index("Honors-Awards")
    except ValueError as e:
        pass

    return start_index


def get_publications_index(resume_list):
    start_index = None
    try:
        start_index = resume_list.index("Publications")
    except ValueError as e:
        pass

    return start_index


def get_patents_index(resume_list):
    start_index = None
    try:
        start_index = resume_list.index("Patents")
    except ValueError as e:
        pass

    return start_index


def get_summary_index(resume_list):
    # Resumo Summary Résumé Samenvatting
    start_index = None
    try:
        start_index = resume_list.index("Resumo")
    except ValueError as e:
        pass

    try:
        start_index = resume_list.index("Summary")
    except ValueError as e:
        pass

    try:
        start_index = resume_list.index("Résumé")
    except ValueError as e:
        pass

    try:
        start_index = resume_list.index("Samenvatting")
    except ValueError as e:
        pass

    if start_index is None:
        return start_index
    else:
        return start_index-5


def get_experience_index(resume_list):
    # Experiência = Experience Expérience Berufserfahrung Ervaring
    start_index = None
    try:
        start_index = resume_list.index("Experiência")
    except ValueError as e:
        pass

    try:
        start_index = resume_list.index("Experience")
    except ValueError as e:
        pass

    try:
        start_index = resume_list.index("Expérience")
    except ValueError as e:
        pass

    try:
        start_index = resume_list.index("Berufserfahrung")
    except ValueError as e:
        pass

    try:
        start_index = resume_list.index("Ervaring")
    except ValueError as e:
        pass

    return start_index


def get_education_index(resume_list):
    # Education Formation Ausbildung Opleiding
    start_index = None
    try:
        start_index = resume_list.index("Education")
    except ValueError as e:
        pass

    try:
        start_index = resume_list.index("Formation")
    except ValueError as e:
        pass

    try:
        start_index = resume_list.index("Ausbildung")
    except ValueError as e:
        pass

    try:
        start_index = resume_list.index("Opleiding")
    except ValueError as e:
        pass

    return start_index


def get_activity_index(resume_list):
    # Activity Activité Aktivitäten Activiteit
    start_index = None
    try:
        start_index = resume_list.index("Activity")
    except ValueError as e:
        pass

    try:
        start_index = resume_list.index("Activité")
    except ValueError as e:
        pass

    try:
        start_index = resume_list.index("Aktivitäten")
    except ValueError as e:
        pass

    try:
        start_index = resume_list.index("Activiteit")
    except ValueError as e:
        pass

    return start_index


def build_resume_index(resume_list):
    contact_start_index = get_contact_index(resume_list)
    summary_start_index = get_summary_index(resume_list)
    activity_start_index = get_activity_index(resume_list)
    education_start_index = get_education_index(resume_list)
    languages_start_index = get_languages_index(resume_list)
    experience_start_index = get_experience_index(resume_list)
    top_skills_start_index = get_top_skills_index(resume_list)
    certifications_start_index = get_certifications_index(resume_list)
    honors_awards_start_index = get_honors_awards_index(resume_list)
    publications_start_index = get_publications_index(resume_list)
    patents_start_index = get_patents_index(resume_list)

    index_list = [
        {"name": "contact", "start": contact_start_index, "end": None}
        , {"name": "summary", "start": summary_start_index, "end": None}
        , {"name": "activity", "start": activity_start_index, "end": None}
        , {"name": "education", "start": education_start_index, "end": None}
        , {"name": "languages", "start": languages_start_index, "end": None}
        , {"name": "experience", "start": experience_start_index, "end": None}
        , {"name": "top_skills", "start": top_skills_start_index, "end": None}
        , {"name": "certifications", "start": certifications_start_index, "end": None}
        , {"name": "honors_awards", "start": honors_awards_start_index, "end": None}
        , {"name": "publications", "start": publications_start_index, "end": None}
        , {"name": "patents", "start": patents_start_index, "end": None}
    ]

    sorted_index = sorted(index_list, key=lambda x: (x['start'] is not None, x['start']), reverse=True)

    index_copy = sorted_index

    last_section = None
    for index, item in enumerate(sorted_index, start=0):
        if item["start"] is None:
            continue
        if last_section is None:
            item["end"] = len(resume_list)
            last_section = index
            index_copy[index] = item
            continue
        else:
            item["end"] = sorted_index[last_section]["start"] - 1
            index_copy[index] = item
            last_section = index

    return index_copy


def test_index(index_copy, resume_list):
    for i in sorted(index_copy, key=lambda x: (x['start'] is not None, x['start']), reverse=False):
        if i['start'] is not None:
            if i['name'] == 'summary':
                print(i['name'], resume_list[i['start']:i['end'] + 1])
            else:
                print(i['name'], resume_list[i['start'] + 1:i['end'] + 1])
    # Contact
    return None


def parse_activity(result_list):
    return None


def parse_education(result_list_slice):
    education_list = []

    def init_education():
        education = {'school': None, 'degree': None}
        return education

    education = init_education()
    for line in result_list_slice:
        if line == '':
            if education['school'] is not None and education['degree'] is not None:
                education_list.append(education)
            education = init_education()
        elif line != '':
            if education['school'] is None:
                education['school'] = line
            elif education['degree'] is None:
                education['degree'] = line

    return education_list


#TO-DO: Handle multi-line sections (e.g., the title is longer than one line)
def parse_experience(result_list_slice):
    import re
    experience_list = []

    def get_indices(x: list, value: int) -> list:
        indices = list()
        i = 0
        while True:
            try:
                # find an occurrence of value and update i to that index
                i = x.index(value, i)
                # add i to the list
                indices.append(i)
                # advance i by 1
                i += 1
            except ValueError as e:
                break
        return indices

    def get_timeline(timeline):
        from datetime import datetime
        start, end, duration = None, None, None
        try:
            split_line = timeline.split('-')
            start_str = split_line[0]
            s = split_line[1]
            end_str = s[0:s.find('(')]
            duration_str = s[s.find('(') + 1:s.find(')')]

            mask = '%B %Y'
            try:
                dt1 = datetime.strptime(start_str, mask)
            except ValueError:
                dt1 = None
            try:
                dt2 = datetime.strptime(end_str, mask)
            except ValueError:
                dt2 = datetime.today()

            if dt1 is not None and dt2 is not None:
                start = dt1.timestamp()
                end = dt2.timestamp()
                duration = (dt2 - dt1).days

        except IndexError:
            # print(f"Error: could not split {line}")
            pass

        return start, end, duration

    def init_experience():
        experience = {'company': None, 'position': None, 'start': None, 'end': None, 'duration': None, 'location': None}
        return experience

    experience = init_experience()
    continued_experience = False
    continued_name = None
    previous_line = None
    ce_regex = re.compile("^[0-9 years]*[0-9 months]*$")

    section_length = len(result_list_slice)
    empty_list = get_indices(result_list_slice, "")
    number_empty = len(empty_list)
    assert number_empty == result_list_slice.count('')
    experience_block, index = 0, 0
    while experience_block < number_empty or index < section_length:
        line = result_list_slice[index]
        #print(line)
        if line == "":
            if experience['company'] is not None and experience['position'] is not None and experience['start'] is not None:
                experience_list.append(experience)
                experience = init_experience()
            experience_block += 1
            index += 1
        else:
            current_segment = empty_list[experience_block] - index
            segment_iter = range(0, current_segment)
            for current_line in segment_iter:
                if ce_regex.search(result_list_slice[index + current_line]) is not None:
                    continued_experience = True

            if current_segment >= 3:
                if continued_experience is True:
                    if ce_regex.search(result_list_slice[index + 1]) is not None:
                        experience['company'] = result_list_slice[index + 0]
                        continued_name = result_list_slice[index + 0]
                        experience['position'] = result_list_slice[index + 2]
                        experience['start'], experience['end'], experience['duration'] = get_timeline(
                            result_list_slice[index + 3])
                        experience['location'] = result_list_slice[index + 4]
                    else:
                        experience['company'] = continued_name
                        experience['position'] = result_list_slice[index + 0]
                        experience['start'], experience['end'], experience['duration'] = get_timeline(
                            result_list_slice[index + 1])
                        experience['location'] = result_list_slice[index + 2]
                else:
                    experience['company'] = result_list_slice[index + 0]
                    experience['position'] = result_list_slice[index + 1]
                    experience['start'], experience['end'], experience['duration'] = get_timeline(
                        result_list_slice[index + 2])
                    experience['location'] = result_list_slice[index + 3]
            index += current_segment
    return experience_list


def parse_summary(result_list_slice):

    def init_summary():
        summary = {'full_name': None, 'tagline': None, 'location': None, 'summary_paragraph': None}
        return summary

    summary = init_summary()

    for index, line in enumerate(result_list_slice, start=0):
        if index == 0:
            summary['full_name'] = line
        elif line != '' and summary['tagline'] is None:
            summary['tagline'] = line
        elif line != '' and summary['location'] is None:
            summary['location'] = line

        if 3 < index < len(result_list_slice)-1 and line != '' and line != 'Summary':
            if summary['summary_paragraph'] is None:
                summary['summary_paragraph'] = line
            else:
                summary['summary_paragraph'] += line

    return summary


def parse_simple(result_list_slice):
    # Used to parse the following indexes:
    #  top skills
    #  certifications
    #  languages
    #  patents
    #  publications
    #  honors and awards
    simple = []
    for line in result_list_slice:
        if line != '':
            simple.append(line)

    return simple


def parse_contact(result_list_slice):
    import re

    def init_contact():
        contact = {'email': None, 'phone': None, 'linkedin_url': None}
        return contact

    contact = init_contact()
    email_regex = re.compile('\S+@\S+')
    linkedin_regex = re.compile("^[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9()@:%_\\+.~#?&\\/=]*)$")
    phone_regex = re.compile('((?:\+\d{2}[-\.\s]??|\d{4}[-\.\s]??)?(?:\d{3}[-\.\s]??\d{3}[-\.\s]??\d{4}|\(\d{3}\)\s*\d{3}[-\.\s]??\d{4}|\d{3}[-\.\s]??\d{4}))')
    for line in result_list_slice:
        if email_regex.search(line) is not None:
            contact['email'] = line
        elif linkedin_regex.search(line) is not None:
            contact['linkedin_url'] = line
        elif phone_regex.search(line) is not None:
            contact['phone'] = line

    return contact


def parse(resume):
    imagewriter = None
    caching = True
    laparams = LAParams()
    retstr = io.StringIO()
    rsrcmgr = PDFResourceManager(caching=caching)
    device = TextConverter(rsrcmgr, retstr, laparams=laparams, imagewriter=imagewriter)

    interpreter = PDFPageInterpreter(rsrcmgr, device)
    for page in PDFPage.get_pages(resume, caching=caching, check_extractable=True):
        interpreter.process_page(page)
        data = retstr.getvalue()

    max_pages = 8
    pages = []
    for num_pages in range(max_pages, 0, -1):
        for page in range(1, num_pages + 1):
            pages.append(f'Page {page} of {num_pages}')

    weird = (
        ["\xa0", "\uf0da", "\x0c", "• ", "* ", "(LinkedIn)", u"\u00b7"
                                                             " (LinkedIn)", "\uf0a7", "(Mobile)", "-       ", "●", "·"]
    )

    weird += pages

    for i in weird:
        data = data.replace(i, "")

    result_list = data.split('\n')
    index = build_resume_index(result_list)

    #convert list to dictionary
    index_d = {item['name']:item for item in index}

    # summary is special due to name fields above start of index
    try:
        summary = parse_summary(result_list[index_d['summary']['start']:min(len(result_list), index_d['summary']['end']+1)])
    except TypeError:
        summary = None

    try:
        contact = parse_contact(result_list[index_d['contact']['start']+1:min(len(result_list), index_d['contact']['end']+1)])
    except TypeError:
        contact = None

    try:
        experience = parse_experience(result_list[index_d['experience']['start']+1:min(len(result_list), index_d['experience']['end']+1)])
    except TypeError:
        experience = None

    try:
        education = parse_education(result_list[index_d['education']['start']+1:min(len(result_list), index_d['education']['end']+1)])
    except TypeError:
        education = None

    try:
        top_skills = parse_simple(result_list[index_d['top_skills']['start']+1:min(len(result_list), index_d['top_skills']['end']+1)])
    except TypeError:
        top_skills = None

    try:
        languages = parse_simple(result_list[index_d['languages']['start']+1:min(len(result_list), index_d['languages']['end']+1)])
    except TypeError:
        languages = None

    try:
        patents = parse_simple(result_list[index_d['patents']['start']+1:min(len(result_list), index_d['patents']['end']+1)])
    except TypeError:
        patents = None

    try:
        certifications = parse_simple(result_list[index_d['certifications']['start']+1:min(len(result_list), index_d['certifications']['end']+1)])
    except TypeError:
        certifications = None

    try:
        publications = parse_simple(result_list[index_d['publications']['start']+1:min(len(result_list), index_d['publications']['end']+1)])
    except TypeError:
        publications = None

    try:
        activity = parse_activity(result_list[index_d['activity']['start']+1:min(len(result_list), index_d['activity']['end']+1)])
    except TypeError:
        activity = None

    try:
        honors_awards = parse_simple(result_list[index_d['honors_awards']['start']+1:min(len(result_list), index_d['honors_awards']['end']+1)])
    except TypeError:
        honors_awards = None

    parsed_resume = {
        'summary': summary,
        'contact': contact,
        'experience': experience,
        'education': education,
        'top_skills': top_skills,
        'languages': languages,
        'patents': patents,
        'certifications': certifications,
        'publications': publications,
        'activity': activity,
        'honors_awards': honors_awards,
        'raw_data': data
    }

    device.close()
    retstr.close()

    return parsed_resume

