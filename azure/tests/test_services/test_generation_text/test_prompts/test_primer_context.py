from unittest.mock import mock_open, patch
from services.generation_text.prompts.primer_context import PrimerContext


def test_set_default_primer():
    primer_context = PrimerContext()
    default_primer = primer_context.set_default_primer(primer="You are Eris MischiefBloom...")
    assert default_primer["role"] == "system"
    assert default_primer["content"] == "You are Eris MischiefBloom..."


def test_get_primer_list():
    read_data = '{"primer": {"role": "system", "content": "You are Eris MischiefBloom..."}}\n'
    m = mock_open(read_data=read_data)

    with patch("builtins.open", m):
        primer_context = PrimerContext()
        primer_list = primer_context.get_primer_list()
        assert len(primer_list) == 1
        assert primer_list[0]["role"] == "system"
        assert primer_list[0]["content"] == "You are Eris MischiefBloom..."


def test_write_primer_list():
    write_data = [{"role": "system", "content": "You are Eris MischiefBloom..."}]
    m = mock_open()

    with patch("builtins.open", m):
        primer_context = PrimerContext()
        primer_context.write_primer_list(write_data)
        m().write.assert_called_once_with(
            '{"primer": {"role": "system", "content": "You are Eris MischiefBloom..."}}\n'
        )


def test_add_primer():
    new_primer = {"role": "user", "content": "I am a user..."}
    read_data = '{"primer": {"role": "system", "content": "You are Eris MischiefBloom..."}}\n'
    m = mock_open(read_data=read_data)

    with patch("builtins.open", m):
        primer_context = PrimerContext()
        primer_context.add_primer(new_primer)
        m().write.assert_called_with('{"primer": {"role": "user", "content": "I am a user..."}}\n')
