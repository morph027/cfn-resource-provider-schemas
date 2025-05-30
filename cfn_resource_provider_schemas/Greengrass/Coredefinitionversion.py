SCHEMA = {
  "typeName" : "AWS::Greengrass::CoreDefinitionVersion",
  "description" : "Resource Type definition for AWS::Greengrass::CoreDefinitionVersion",
  "additionalProperties" : False,
  "properties" : {
    "Id" : {
      "type" : "string"
    },
    "Cores" : {
      "type" : "array",
      "uniqueItems" : False,
      "items" : {
        "$ref" : "#/definitions/Core"
      }
    },
    "CoreDefinitionId" : {
      "type" : "string"
    }
  },
  "definitions" : {
    "Core" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "SyncShadow" : {
          "type" : "boolean"
        },
        "ThingArn" : {
          "type" : "string"
        },
        "Id" : {
          "type" : "string"
        },
        "CertificateArn" : {
          "type" : "string"
        }
      },
      "required" : [ "ThingArn", "Id", "CertificateArn" ]
    }
  },
  "required" : [ "Cores", "CoreDefinitionId" ],
  "createOnlyProperties" : [ "/properties/Cores", "/properties/CoreDefinitionId" ],
  "primaryIdentifier" : [ "/properties/Id" ],
  "readOnlyProperties" : [ "/properties/Id" ]
}