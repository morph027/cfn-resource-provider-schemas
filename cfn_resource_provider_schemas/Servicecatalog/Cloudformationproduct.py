SCHEMA = {
  "typeName" : "AWS::ServiceCatalog::CloudFormationProduct",
  "description" : "Resource Type definition for AWS::ServiceCatalog::CloudFormationProduct",
  "additionalProperties" : False,
  "properties" : {
    "Owner" : {
      "type" : "string"
    },
    "Description" : {
      "type" : "string"
    },
    "ProductName" : {
      "type" : "string"
    },
    "SupportEmail" : {
      "type" : "string"
    },
    "ProductType" : {
      "type" : "string"
    },
    "ProvisioningArtifactNames" : {
      "type" : "string"
    },
    "Name" : {
      "type" : "string"
    },
    "ReplaceProvisioningArtifacts" : {
      "type" : "boolean"
    },
    "SupportDescription" : {
      "type" : "string"
    },
    "Distributor" : {
      "type" : "string"
    },
    "ProvisioningArtifactIds" : {
      "type" : "string"
    },
    "AcceptLanguage" : {
      "type" : "string"
    },
    "SupportUrl" : {
      "type" : "string"
    },
    "Id" : {
      "type" : "string"
    },
    "SourceConnection" : {
      "$ref" : "#/definitions/SourceConnection"
    },
    "Tags" : {
      "type" : "array",
      "uniqueItems" : False,
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    },
    "ProvisioningArtifactParameters" : {
      "type" : "array",
      "uniqueItems" : False,
      "items" : {
        "$ref" : "#/definitions/ProvisioningArtifactProperties"
      }
    }
  },
  "definitions" : {
    "CodeStarParameters" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "ArtifactPath" : {
          "type" : "string"
        },
        "ConnectionArn" : {
          "type" : "string"
        },
        "Repository" : {
          "type" : "string"
        },
        "Branch" : {
          "type" : "string"
        }
      },
      "required" : [ "ArtifactPath", "Repository", "Branch", "ConnectionArn" ]
    },
    "ConnectionParameters" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "CodeStar" : {
          "$ref" : "#/definitions/CodeStarParameters"
        }
      }
    },
    "ProvisioningArtifactProperties" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Type" : {
          "type" : "string"
        },
        "Description" : {
          "type" : "string"
        },
        "Info" : {
          "type" : "object"
        },
        "DisableTemplateValidation" : {
          "type" : "boolean"
        },
        "Name" : {
          "type" : "string"
        }
      },
      "required" : [ "Info" ]
    },
    "Tag" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Value" : {
          "type" : "string"
        },
        "Key" : {
          "type" : "string"
        }
      },
      "required" : [ "Value", "Key" ]
    },
    "SourceConnection" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "ConnectionParameters" : {
          "$ref" : "#/definitions/ConnectionParameters"
        },
        "Type" : {
          "type" : "string"
        }
      },
      "required" : [ "Type", "ConnectionParameters" ]
    }
  },
  "required" : [ "Owner", "Name" ],
  "primaryIdentifier" : [ "/properties/Id" ],
  "readOnlyProperties" : [ "/properties/ProvisioningArtifactIds", "/properties/Id", "/properties/ProvisioningArtifactNames", "/properties/ProductName" ]
}