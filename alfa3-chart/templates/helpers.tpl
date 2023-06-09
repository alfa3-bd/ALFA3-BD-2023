{{- define "alfa3-chart.getImage" }}
{{- $imageName := .Values.alfa3-bd.image.repository }}
{{- $tag := .Values.alfa3-bd.image.tag }}
{{- printf "%s:%s" $imageName $tag }}
{{- end }}