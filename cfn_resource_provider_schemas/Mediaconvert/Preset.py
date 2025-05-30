SCHEMA = {
  "typeName" : "AWS::MediaConvert::Preset",
  "description" : "Resource Type definition for AWS::MediaConvert::Preset",
  "additionalProperties" : False,
  "properties" : {
    "Category" : {
      "type" : "string"
    },
    "Description" : {
      "type" : "string"
    },
    "SettingsJson" : {
      "type" : "object"
    },
    "Id" : {
      "type" : "string"
    },
    "Arn" : {
      "type" : "string"
    },
    "Tags" : {
      "type" : "object"
    },
    "Name" : {
      "type" : "string"
    }
  },
  "required" : [ "SettingsJson" ],
  "createOnlyProperties" : [ "/properties/Name" ],
  "primaryIdentifier" : [ "/properties/Id" ],
  "readOnlyProperties" : [ "/properties/Id", "/properties/Arn" ]
}