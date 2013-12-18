# please hire me
a Django app for building an online portfolio and resume

## requirements
*	Python 2.7x
*	Django 1.5x

###django app dependencies
*	django-embed-video
*	django-polymorphic

## data model
**Project**

*	name
*	slug (url-safe version of name)
*	order
*	date
*	summary
*	context (relation to a **Context**, see below)
*	details (relations to one or more **ProjectDetails**, see below)

**Detail**

*	name
*	order
*	description
*	*types of Details:*
	*	**ProjectDetail**
		* parent (relation to a **Project**)
		* *types of ProjectDetails:*
			* **ImageUpload**
				* file
			* **VideoEmbed**
				* video url (handled by django-embed-video app)
			* **Bullet** (no additional fields)
	* **JobDetail**
		* parent (relation to a **Job**, see below)
	* **SchoolDetail**
		* parent (relation to a **School**, see below)
	* **SkillArea**
		* skills (relations to one or more **Skills**)
	* **Skill**
		* parent (relation to a **SkillArea**)
	* **Award**
		* organization
		* date

**Context**

* name
* slug
* *types of Contexts:*
	* generic
	* **Job**
		* organization
		* startdate
		* enddate (optional)
		* location
		* details (relations to one or more **JobDetails**)
	* **School**
		* location
		* degree
		* startdate
		* enddate
		* details (relations to one or more **SchoolDetails**)
