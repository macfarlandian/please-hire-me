<h3>{{role.name}} <br/>
	<small>{{ role.org }}
		{% if role.location %}
		{{ sep }}
		{{ role.location }}
		{% endif %}
		{% if role.startdate %}
		{{ sep }}
		{{ role.startdate|date:"Y" }}&nbsp;-&nbsp;	
		{% endif %}
		{% if role.enddate %}
		{{ role.enddate|date:"Y" }}
		{% elif role.startdate %}
		present
		{% endif %}
	</small>
</h3>
{{role.long_desc|safe}}
{% if role.projects.all %}
<div class="col-sm-offset-1 clearfix well">
	<div class="row">
		<h4 class="col-sm-12">Projects</h4> 
	</div>

	{% for project in role.projects.all %}
	<div class="row">
		<div class="col-sm-2">
			<h5>
				<a href="{% url 'project' slug=project.slug %}">
					{{ project.name }}
				</a>
			</h5>
		</div>
		{% if project.index_image %}
		<div class="col-sm-3">
			<img src="{{ project.index_image.url }}" alt="{{ project.name }}" class="img-thumbnail img-responsive"/>
		</div>
		<div class="col-sm-7 small">
			{{ project.summary|safe }}
		</div>
		{% else %}
		<div class="col-sm-10 small">
			{{ project.summary|safe }}
		</div>
		{% endif %}
	</div>
	{% endfor %}
</div>
{% endif %}