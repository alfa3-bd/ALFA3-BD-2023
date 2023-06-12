{{- define "alfa3-chart.getImage" }}
{{- $imageName := .Values.containers.alfa3bd.image.repository }}
{{- $tag := .Values.containers.alfa3bd.image.tag }}
{{- printf "%s:%s" $imageName $tag }}
{{- end }}
