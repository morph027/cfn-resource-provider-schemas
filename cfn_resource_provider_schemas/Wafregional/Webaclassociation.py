SCHEMA = {
  "typeName" : "AWS::WAFRegional::WebACLAssociation",
  "description" : "Resource Type definition for AWS::WAFRegional::WebACLAssociation",
  "additionalProperties" : False,
  "properties" : {
    "Id" : {
      "type" : "string"
    },
    "ResourceArn" : {
      "type" : "string"
    },
    "WebACLId" : {
      "type" : "string"
    }
  },
  "required" : [ "ResourceArn", "WebACLId" ],
  "createOnlyProperties" : [ "/properties/ResourceArn", "/properties/WebACLId" ],
  "primaryIdentifier" : [ "/properties/Id" ],
  "readOnlyProperties" : [ "/properties/Id" ]
}