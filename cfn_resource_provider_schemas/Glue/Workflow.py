SCHEMA = {
  "typeName" : "AWS::Glue::Workflow",
  "description" : "Resource Type definition for AWS::Glue::Workflow",
  "additionalProperties" : False,
  "properties" : {
    "Description" : {
      "type" : "string"
    },
    "Id" : {
      "type" : "string"
    },
    "Tags" : {
      "type" : "object"
    },
    "DefaultRunProperties" : {
      "type" : "object"
    },
    "Name" : {
      "type" : "string"
    },
    "MaxConcurrentRuns" : {
      "type" : "integer"
    }
  },
  "createOnlyProperties" : [ "/properties/Name" ],
  "primaryIdentifier" : [ "/properties/Id" ],
  "readOnlyProperties" : [ "/properties/Id" ]
}