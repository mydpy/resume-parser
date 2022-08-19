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


def get_language_index(resume_list):
    start_index = None
    try:
        start_index = resume_list.index("Language")
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
    language_start_index = get_language_index(resume_list)
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
        , {"name": "language", "start": language_start_index, "end": None}
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
            #print(index, "first", item)
            continue
        if last_section is None:
            item["end"] = len(resume_list)
            last_section = index
            index_copy[index] = item
            #print(index, "second", item)
            continue
        else:
            item["end"] = sorted_index[last_section]["start"] - 1
            index_copy[index] = item
            last_section = index
            #print(index, "third", item)

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


def parse_contact(data_list):
    try:
        section_start_index = data_list.index("Contact")
        section_stop_index = data_list.index("Top Skills")
    except Exception as e:
        return
    return


def parse(resume):
    imagewriter = None
    caching = True
    laparams = LAParams()
    retstr = io.StringIO()
    rsrcmgr = PDFResourceManager(caching=caching)
    device = TextConverter(rsrcmgr, retstr, laparams=laparams, imagewriter=imagewriter)
    data = []
    skills = []
    languages = []
    summary = []
    certifications = []
    contact = []
    linkedin = []
    experience = []
    education = []
    complete_experience = []
    complete_education = []
    exp_dict = {}
    edu_dict = {}
    alld = {}

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

    #return {"index": build_resume_index(result_list)}

    lengthOfResultArray = result_list.__len__()
    for i in result_list:
        if i == 'Contact':
            value = result_list.index(i)
            while True:
                value = value + 1
                contact.append(result_list[value].strip())
                if result_list[value] == '':
                    contact.remove(result_list[value])
                    break

        if i.__contains__('www.linkedin.com'):
            value = result_list.index(i)
            while True:
                linkedin.append(result_list[value])
                value = value + 1
                if result_list[value] == '':
                    break
            if len(linkedin) >= 2:
                ln = []
                merged = linkedin[0] + linkedin[1].strip()
                ln.append(merged)
                linkedin = ln

        if i == 'Top Skills':
            value = result_list.index(i)
            while True:
                value = value + 1
                skills.append(result_list[value])
                if result_list[value] == '':
                    skills.remove(result_list[value])
                    break

        if i.__contains__('Certifications'):
            value = result_list.index(i)
            while True:
                value = value + 1
                certifications.append(result_list[value])
                if result_list[value] == '':
                    certifications.remove(result_list[value])
                    break

        if i.__contains__('Summary'):
            value = result_list.index(i)
            while True:
                value = value + 1
                summary.append(result_list[value])
                if result_list[value] == '':
                    summary.remove(result_list[value])
                    break

        if i == 'Languages':
            value = result_list.index(i)
            while True:
                value = value + 1
                languages.append(result_list[value])
                if result_list[value] == '':
                    languages.remove(result_list[value])
                    break

        if i == 'Experience':
            value = result_list.index(i)
            value = value + 2

            while True:
                # Following condition checks if we have reached the end of the file, this is necessary in case if this section is the last section
                if (value >= lengthOfResultArray - 1):
                    break
                # Following condition checks if we have encountered another section that means this section has finished
                if (check_section_start(result_list[value])) is True:
                    break

                if (result_list[value] == ''):
                    value += 1
                    experience = []
                # Following condition checks if the next three non-empty lines of document are: Name of Company, Position, Period, and Location/Place respectively.
                elif (
                        result_list[value - 1] == ""
                        and result_list[value + 1] != ""
                        and result_list[value + 2].__contains__("-")
                ):
                    # If the above condition is true, we can fetch this experience object and save it in complete_experience array.
                    experience.append(result_list[value])  # Company Name
                    experience.append(result_list[value + 1])  # Job Title
                    experience.append(result_list[value + 2])  # Period
                    experience.append(result_list[value + 3])  # Place
                    listOfExp = ["company", "position", "period", "place"]
                    zipbObj = zip(listOfExp, experience)
                    exp_dict = dict(zipbObj)
                    complete_experience.append(exp_dict)
                    experience = []
                    # As we have fetched 4 indexes in above code, and we know the value at fifth index can either be a description or an empty space,
                    # so we increment the counter to 5.
                    value += 5
                else:
                    value += 1

        if i == 'Education':
            value = result_list.index(i)
            value = value + 1
            index = 0
            while True:
                # Following condition checks if we have reached the end of the file, this is necessary in case if this section is the last section
                if (value >= lengthOfResultArray - 1):
                    break
                # Following condition checks if we have encountered another section that means this section has finished
                if (check_section_start(result_list[value])) is True:
                    break

                if result_list[value] == '':
                    value = value + 1
                else:
                    education.append(result_list[value])
                    value = value + 1
                    index += 1
                    if (index == 2):
                        # When we have fetched the 2 values(school & degree) in the education array, we can now create an education object from this array
                        listOfEdu = ["school", "degree"]
                        zipbObj = zip(listOfEdu, education)
                        edu_dict = dict(zipbObj)
                        # Save the education object in complete_education array. This complete_education array will have all the education objects
                        complete_education.append(edu_dict)
                        index = 0
                        education = []

    alld['contact'] = contact
    alld['skills'] = skills
    alld['linkedin'] = linkedin[0]
    alld['skills'] = skills
    alld['certifications'] = certifications
    alld['summary'] = summary
    alld['languages'] = languages
    alld['experience'] = complete_experience
    alld['education'] = complete_education
    alld['raw_data'] = data
    alld['index'] = build_resume_index(result_list)
    device.close()
    retstr.close()

    return alld
