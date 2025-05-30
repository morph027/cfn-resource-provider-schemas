SCHEMA = {
  "typeName" : "AWS::Pinpoint::EmailTemplate",
  "description" : "Resource Type definition for AWS::Pinpoint::EmailTemplate",
  "additionalProperties" : False,
  "properties" : {
    "HtmlPart" : {
      "type" : "string"
    },
    "TextPart" : {
      "type" : "string"
    },
    "TemplateName" : {
      "type" : "string"
    },
    "TemplateDescription" : {
      "type" : "string"
    },
    "DefaultSubstitutions" : {
      "type" : "string"
    },
    "Id" : {
      "type" : "string"
    },
    "Arn" : {
      "type" : "string"
    },
    "Subject" : {
      "type" : "string"
    },
    "Tags" : {
      "type" : "object"
    }
  },
  "required" : [ "TemplateName", "Subject" ],
  "createOnlyProperties" : [ "/properties/TemplateName" ],
  "primaryIdentifier" : [ "/properties/Id" ],
  "readOnlyProperties" : [ "/properties/Id", "/properties/Arn" ]
}