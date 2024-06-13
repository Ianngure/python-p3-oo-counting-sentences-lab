#!/usr/bin/env python3

class MyString:
    def __init__(self, value=''):
        self._value = ''
        self.value = value

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, new_value):
        if isinstance(new_value, str):
            self._value = new_value
        else:
            print("The value must be a string.")
            self._value = ''

    def is_sentence(self):
        return self.value.endswith('.')

    def is_question(self):
        return self.value.endswith('?')

    def is_exclamation(self):
        return self.value.endswith('!')

    def count_sentences(self):
        # Check if value is an empty string
        if not self.value:
            return 0
        
        # Replace exclamation marks and question marks with periods
        cleaned_value = self.value.replace('!', '.').replace('?', '.')
        # Split by periods
        sentences = cleaned_value.split('.')
        # Remove empty strings from the list
        non_empty_sentences = [s for s in sentences if s.strip()]
        return len(non_empty_sentences)
