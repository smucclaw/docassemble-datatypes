# docassemble-datatypes

In [docassemble](https://docassemble.org), the `objects:` block can be used to declare complicated data
structures, and `generic object:` blocks can be used to interact with those
objects without needing to write separate questions or code blocks for each
instance of that class.

**docassemble-datatypes** makes the same mechanism available for simple data values. If you
need to collect a string, for example, instead of writing a question that collects
the string and assigns the value to a variable, you can use the following line in
an `objects:` block:

`  - info: DADTString`

If you then use the variable `info` anywhere in your interview, a generic
question is provided that will be displayed to the user.

This is useful for fast prototyping of docassemble interviews, and for automatically generating prototype interviews from any system that has typed data structure information.

## Installation

Install from this repository using the docassemble package manager feature.

## Usage

Add the following line to an `include:` block in your interview:

```
  - docassemble.datatypes:DADataTypes.yml
```

Then, add the objects that you want to collect to your `objects:` block:

```
  - this: DADTString
  - that: DADTNumber
  - options: DAList.using(object_type=DADTString)
  - favourite: DADTObjectRef.using(source=options)
```

## Types Available

 * DADTString
 * DADTNumber
 * DADTBoolean
 * DADTContinue
  
  If you collect this value, it will force the user to set the value to True
  before they can continue the interview. This is useful to simulate a terms
  of service requirement.
 * DADTYesNoMaybe
 * DADTEmail
 * DADTFile
 * DADTEnum
  
  A DADTEnum object is a choice between a fixed set of options. To create this
  type you must provide an `options` attribute, which sets out a dictionary
  of options to display, and their internal values. Because of the way YAML
  syntax works, this cannot be on the same line as the object declaration, so
  to create an object that collects either the value `a` or the value `o`, you
  might do this:

  ```
  objects:
    - favourite_fruit: |
        DADTEnum.using(options={'o': 'Oranges', 'a': 'Apples'})
  ```
 * DADTObjectRef
  
  A DADTObjectRef is a reference to an object that was collected in another DAList.  To create this type, you must provide a `source` attribute that
  refers to a DAList object as follows:
  ```
  objects:
    - person: DAList.using(object_type=Person)
    - favourite: DADTObjectRef.using(source=person)
  ```
