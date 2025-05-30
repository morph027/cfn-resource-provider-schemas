SCHEMA = {
  "typeName" : "AWS::CloudFormation::WaitCondition",
  "description" : "Resource Type definition for AWS::CloudFormation::WaitCondition",
  "additionalProperties" : False,
  "properties" : {
    "Id" : {
      "type" : "string"
    },
    "Data" : {
      "type" : "object"
    },
    "Count" : {
      "type" : "integer"
    },
    "Handle" : {
      "type" : "string"
    },
    "Timeout" : {
      "type" : "string"
    }
  },
  "readOnlyProperties" : [ "/properties/Data", "/properties/Id" ],
  "primaryIdentifier" : [ "/properties/Id" ]
}