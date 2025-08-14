# Week Module Generator Scripts

This directory contains scripts to help manage Jekyll week module files for the course website.

## Scripts Overview

### 1. `migrate_stash.py` - Migrate Existing Files
Moves all week files from `_module_stash/` to `_modules/` directory.

```bash
python3 scripts/migrate_stash.py
```

This will:
- Copy all `week-*.md` files from `_module_stash/` to `_modules/`
- Create the `_modules/` directory if it doesn't exist
- Preserve original files in `_module_stash/` (you can delete them manually after verification)

### 2. `generate_week.py` - Generate New Week Files
Creates new week module files with proper Jekyll formatting.

#### Basic Usage (Empty Template)
```bash
python3 scripts/generate_week.py 1 "Python Basics" 2023-10-02
```

#### With Common Event Structure
```bash
python3 scripts/generate_week.py 1 "Python Basics" 2023-10-02 --template
```

The `--template` flag generates a week with typical course events:
- Monday: Lecture
- Wednesday: Lecture + Discussion
- Friday: Lecture
- Sunday: Homework due

## Generated File Structure

The scripts generate files with the following structure:

```yaml
---
    title: Week 1 – Python Basics
    weekNumber: 1
    days:
      - date: 2023-10-2
        events:
          "**LEC 2**{: .label .label-lecture } [Topic Title](datahub-link) [✏️](html-link)":
            "[Reading Reference](link)"
          "<small><i><span style='display: inline-block; padding-left: 80px'><b>Keywords:</b> keyword1, keyword2</span></i></small>":
---
```

## Event Types Supported

The generator supports all common course event types:

- **LEC** - Lectures (with DataHub links, HTML versions, readings, keywords)
- **DIS** - Discussions (with practice links)
- **LAB** - Labs (with notebook links)
- **HW** - Homework (with assignment links)
- **QUIZ** - Quizzes (with optional solution links)
- **EXAM** - Exams
- **PROJ** - Projects (with partner guidelines)
- **SUR** - Surveys (with Google Forms links)

## Workflow Recommendation

1. **First time setup**: Run `migrate_stash.py` to move existing files
2. **For new weeks**: Use `generate_week.py` with `--template` flag
3. **Edit generated files**: Customize the template with actual content
4. **Delete `_module_stash/`**: Once you're confident everything works

## Benefits Over Manual Copying

- **Consistency**: All files follow the same format and structure
- **Speed**: Generate new weeks in seconds instead of minutes
- **Accuracy**: Reduces copy-paste errors and formatting issues
- **Maintainability**: Easy to update the template for all future weeks
- **Automation**: Can be integrated into build scripts or workflows 