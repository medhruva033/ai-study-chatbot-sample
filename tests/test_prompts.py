from src.prompts import (
    SUBJECTS,
    STUDY_MODES,
    build_system_prompt,
)


def test_prompt_contains_subject():
    prompt = build_system_prompt(
        subject="DBMS",
        study_mode="Explain",
    )

    assert "DBMS" in prompt


def test_prompt_contains_study_mode():
    prompt = build_system_prompt(
        subject="DSA",
        study_mode="Interview",
    )

    assert "Interview" in prompt


def test_all_subjects_are_available():
    assert "DSA" in SUBJECTS
    assert "DBMS" in SUBJECTS


def test_all_study_modes_are_available():
    assert "Explain" in STUDY_MODES
    assert "Quiz Me" in STUDY_MODES
    assert "Interview" in STUDY_MODES
    assert "Coding Problem" in STUDY_MODES


def test_prompt_has_tutor_instructions():
    prompt = build_system_prompt(
        subject="Operating Systems",
        study_mode="Explain",
    )

    assert "AI Study Tutor" in prompt
    assert "step by step" in prompt