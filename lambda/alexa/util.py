# -*- coding: utf-8 -*-

"""Utility module to generate text for commonly used responses."""

import random
import six
from ask_sdk_core.handler_input import HandlerInput
from ask_sdk_core.utils import is_request_type

from . import data


def get_ordinal_indicator(counter):
    """Return st, nd, rd, th ordinal indicators according to counter."""
    if counter == 1:
        return "{}st".format(str(counter))
    elif counter == 2:
        return "{}nd".format(str(counter))
    elif counter == 3:
        return "{}rd".format(str(counter))
    else:
        return "{}th".format(str(counter))


def __get_attr_for_speech(attr):
    """Helper function to convert attribute name."""
    return attr.lower().replace("_", " ").strip()


def get_question_without_ordinal(index):
    return data.QUESTIONS_LIST[index]['q'] + "," + get_multiple_choice_answers(index)


def get_question(counter):
    """Return response text for nth question to the user."""
    return (
        "Here is your {} question. {}").format(
        get_ordinal_indicator(counter+1),
        get_question_without_ordinal(counter))


def ask_question(handler_input):
    # (HandlerInput) -> None
    """Return next question from the question list."""
    attr = handler_input.attributes_manager.session_attributes
    handler_input.attributes_manager.session_attributes = attr
    
    # Update counter for next question
    attr['counter'] += 1
    
    return get_question(attr["counter"])


def get_speechcon(neutral, singular):
    """Return speechcon corresponding to the boolean answer correctness."""
    if neutral:
        return random.choice(data.NEUTRAL_SPEECHCONS)
    else:
        if singular:
            return random.choice(data.SINGULAR_AGREE_SPEECHCONS)
        return random.choice(data.PLURAL_AGREE_SPEECHCONS)


def get_multiple_choice_answers(counter):
    """Return multiple choices for the display to show."""
    answers_list = ""
    # Insert the correct answer first
    answer_choices = data.QUESTIONS_LIST[counter]['a']
    letters = ['a', 'b', 'c', 'd']
    for letter, choice in zip(letters, answer_choices):
        answers_list += " " + letter + ", " + choice + ", "
    return answers_list


