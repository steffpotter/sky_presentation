from application.dao.baseDao import BaseDao
from subject import Subject
from question import Question
from answer import Answer




class SubjectDao(BaseDao):

    """
    DAO class for Subject objects - The DAO pattern offers a layer of abstraction between the database
    and the application. This gives the dev team the freedom to evolve the db and business/ application layer separately.
    """

    def __init__(self, useMock):
        super().__init__(useMock)

    def getAllSubjects(self):
        """ Returns a list of Subject objects."""
        subjects = self._db.getAllSubjects()
        # returns list of dictionaries corresponding to Subject rows in db
        # map subject dictionaries to Subject Python object using a list comprehension
        subjectObjs = [Subject(subject.get("subject_id"),
                               subject.get("subject_name"),
                               subject.get("subject_logo"),
                               subject.get("subject_content"),
                       [Question(question.get("question_id"), 
                                 question.get("question_text"), 
                                 question.get("correct_answer_id"),
                                 [Answer(answer.get("answer_id"), 
                                         answer.get("answer_text")) for answer in question.get("answers")]) 
                                         for question in subject.get("subject_questions")])                       
                                 for subject in subjects]
        return subjectObjs

    def getSubject(self, subjectId):
        subject = self._db.getSubject(subjectId)  # todo - test how mysql connector handles error when no subject found
        
        try:
            return Subject(subjectId,
                        subject.get("subject_name"),
                        subject.get("subject_logo"),
                        subject.get("subject_content"),
                        [Question(question.get("question_id"), 
                                    question.get("question_text"), 
                                    question.get("correct_answer_id"),
                                    [Answer(answer.get("answer_id"), 
                                            answer.get("answer_text")) for answer in question.get("answers")]) 
                                    for question in subject.get("subject_questions")])
        except Exception as e:
            print("Error in getSubjectByName: ", e)


    # Can extend to have Add, Update and Delete functions below
