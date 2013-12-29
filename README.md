# please hire me
a Django app for building an online portfolio and resume

## requirements
*	Python 2.7x
*	Django 1.5x

###django app dependencies
* django-embed-video
* django-grappelli

## data model

**Project**

*	name
*	slug (url-safe version of name)
*	order
*	date
*	summary

**Detail**

* name
* order
* description
* image file
* video url (handled by django-embed-video app)
	

**Context**

* name
* slug
* organization
* startdate
* enddate
* location
* description

**Resume**
scaffolding for arranging your **Jobs **and other **Contexts**

* name
* address
* phone
* email
* website
* linkedin
* twitter


* **Blocks**
assembled to form a **Resume**

* name
* description

		
		
## relationship architecture

**Project**:

* CONTAINS one or more **Details**
* RELATED TO one **Context**

**Context** (job, school, etc):

* RELATED TO zero or more **Projects**

**Portfolio**:

* INCLUDES one or more **Projects**

**Resume**:

* CONTAINS one or more **Blocks**

**Block** 

Summary form:

* no relations

Collection form:

* INCLUDES one or more **Contexts**
* INCLUDES zero or more **Collection Blocks** (nesting)