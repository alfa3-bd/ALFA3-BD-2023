{{- define "alfa3-chart.getImage" }}
{{- $imageName := .Values.alfa3bd.image.repository }}
{{- $tag := .Values.alfa3bd.image.tag }}
{{- printf "%s:%s" $imageName $tag }}
{{- end }}
