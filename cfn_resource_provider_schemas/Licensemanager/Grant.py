SCHEMA = {
  "typeName" : "AWS::LicenseManager::Grant",
  "description" : "An example resource schema demonstrating some basic constructs and validation rules.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-rpdk.git",
  "definitions" : {
    "Arn" : {
      "type" : "string",
      "maxLength" : 2048
    }
  },
  "properties" : {
    "GrantArn" : {
      "description" : "Arn of the grant.",
      "$ref" : "#/definitions/Arn"
    },
    "GrantName" : {
      "description" : "Name for the created Grant.",
      "type" : "string"
    },
    "LicenseArn" : {
      "description" : "License Arn for the grant.",
      "$ref" : "#/definitions/Arn"
    },
    "HomeRegion" : {
      "description" : "Home region for the created grant.",
      "type" : "string"
    },
    "Version" : {
      "description" : "The version of the grant.",
      "type" : "string"
    },
    "AllowedOperations" : {
      "type" : "array",
      "uniqueItems" : True,
      "items" : {
        "type" : "string"
      }
    },
    "Principals" : {
      "type" : "array",
      "uniqueItems" : True,
      "items" : {
        "$ref" : "#/definitions/Arn"
      }
    },
    "Status" : {
      "type" : "string"
    }
  },
  "additionalProperties" : False,
  "required" : [ ],
  "readOnlyProperties" : [ "/properties/GrantArn", "/properties/Version" ],
  "writeOnlyProperties" : [ "/properties/Principals", "/properties/AllowedOperations", "/properties/Status" ],
  "primaryIdentifier" : [ "/properties/GrantArn" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "license-manager:CreateGrant" ]
    },
    "read" : {
      "permissions" : [ "license-manager:GetGrant" ]
    },
    "update" : {
      "permissions" : [ "license-manager:CreateGrantVersion" ]
    },
    "delete" : {
      "permissions" : [ "license-manager:DeleteGrant" ]
    },
    "list" : {
      "permissions" : [ "license-manager:ListDistributedGrants" ]
    }
  }
}