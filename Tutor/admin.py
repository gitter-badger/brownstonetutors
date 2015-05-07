from django.contrib import admin
from models import Tutor, TutorStudentRelationship, Session, TutorStudentSubjectRate

class TutorStudentSubjectRateInline(admin.TabularInline):
	model = TutorStudentSubjectRate
	extra = 0

class TutorStudentRelationshipAdmin(admin.ModelAdmin):
	inlines = (TutorStudentSubjectRateInline,)

admin.site.register(Tutor)
admin.site.register(TutorStudentRelationship, TutorStudentRelationshipAdmin)
admin.site.register(TutorStudentSubjectRate)
admin.site.register(Session)