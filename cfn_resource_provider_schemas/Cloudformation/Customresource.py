SCHEMA = {
  "typeName" : "AWS::CloudFormation::CustomResource",
  "description" : "Resource Type definition for AWS::CloudFormation::CustomResource",
  "additionalProperties" : False,
  "properties" : {
    "ServiceToken" : {
      "type" : "string"
    },
    "ServiceTimeout" : {
      "type" : "integer"
    },
    "Id" : {
      "type" : "string"
    }
  },
  "required" : [ "ServiceToken" ],
  "createOnlyProperties" : [ "/properties/ServiceToken" ],
  "primaryIdentifier" : [ "/properties/Id" ],
  "readOnlyProperties" : [ "/properties/Id" ]
}