SCHEMA = {
  "typeName" : "AWS::ServiceCatalog::TagOption",
  "description" : "Resource Type definition for AWS::ServiceCatalog::TagOption",
  "additionalProperties" : False,
  "properties" : {
    "Id" : {
      "type" : "string"
    },
    "Active" : {
      "type" : "boolean"
    },
    "Value" : {
      "type" : "string"
    },
    "Key" : {
      "type" : "string"
    }
  },
  "required" : [ "Value", "Key" ],
  "createOnlyProperties" : [ "/properties/Value", "/properties/Key" ],
  "primaryIdentifier" : [ "/properties/Id" ],
  "readOnlyProperties" : [ "/properties/Id" ]
}