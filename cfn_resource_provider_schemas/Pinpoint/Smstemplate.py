SCHEMA = {
  "typeName" : "AWS::Pinpoint::SmsTemplate",
  "description" : "Resource Type definition for AWS::Pinpoint::SmsTemplate",
  "additionalProperties" : False,
  "properties" : {
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
    "Body" : {
      "type" : "string"
    },
    "Tags" : {
      "type" : "object"
    }
  },
  "required" : [ "TemplateName", "Body" ],
  "createOnlyProperties" : [ "/properties/TemplateName" ],
  "primaryIdentifier" : [ "/properties/Id" ],
  "readOnlyProperties" : [ "/properties/Id", "/properties/Arn" ]
}