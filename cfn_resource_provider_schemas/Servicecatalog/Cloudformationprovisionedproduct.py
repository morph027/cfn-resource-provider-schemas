SCHEMA = {
  "typeName" : "AWS::ServiceCatalog::CloudFormationProvisionedProduct",
  "description" : "Resource Schema for AWS::ServiceCatalog::CloudFormationProvisionedProduct",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-rpdk.git",
  "documentationUrl" : "https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-servicecatalog-cloudformationprovisionedproduct.html",
  "definitions" : {
    "ProvisioningPreferences" : {
      "type" : "object",
      "properties" : {
        "StackSetAccounts" : {
          "type" : "array",
          "uniqueItems" : True,
          "items" : {
            "type" : "string",
            "pattern" : "^[0-9]{12}$"
          }
        },
        "StackSetFailureToleranceCount" : {
          "type" : "integer",
          "minimum" : 0
        },
        "StackSetFailureTolerancePercentage" : {
          "type" : "integer",
          "minimum" : 0,
          "maximum" : 100
        },
        "StackSetMaxConcurrencyCount" : {
          "type" : "integer",
          "minimum" : 1
        },
        "StackSetMaxConcurrencyPercentage" : {
          "type" : "integer",
          "minimum" : 1,
          "maximum" : 100
        },
        "StackSetOperationType" : {
          "type" : "string",
          "enum" : [ "CREATE", "UPDATE", "DELETE" ]
        },
        "StackSetRegions" : {
          "type" : "array",
          "uniqueItems" : True,
          "items" : {
            "type" : "string",
            "pattern" : "^[a-z]{2}-([a-z]+-)+[1-9]"
          }
        }
      },
      "additionalProperties" : False
    },
    "ProvisioningParameter" : {
      "type" : "object",
      "properties" : {
        "Key" : {
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 1000
        },
        "Value" : {
          "type" : "string",
          "maxLength" : 4096
        }
      },
      "additionalProperties" : False,
      "required" : [ "Key", "Value" ]
    },
    "Tag" : {
      "type" : "object",
      "properties" : {
        "Key" : {
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 128,
          "pattern" : "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-@]*)$"
        },
        "Value" : {
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 256,
          "pattern" : "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-@]*)$"
        }
      },
      "additionalProperties" : False,
      "required" : [ "Key", "Value" ]
    },
    "OutputType" : {
      "type" : "string"
    }
  },
  "properties" : {
    "AcceptLanguage" : {
      "type" : "string",
      "enum" : [ "en", "jp", "zh" ]
    },
    "NotificationArns" : {
      "type" : "array",
      "uniqueItems" : True,
      "items" : {
        "type" : "string"
      },
      "maxItems" : 5
    },
    "PathId" : {
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 100
    },
    "PathName" : {
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 100
    },
    "ProductId" : {
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 100
    },
    "ProductName" : {
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 128
    },
    "ProvisionedProductName" : {
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 128
    },
    "ProvisioningArtifactId" : {
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 100
    },
    "ProvisioningArtifactName" : {
      "type" : "string"
    },
    "ProvisioningParameters" : {
      "type" : "array",
      "items" : {
        "$ref" : "#/definitions/ProvisioningParameter"
      }
    },
    "ProvisioningPreferences" : {
      "$ref" : "#/definitions/ProvisioningPreferences"
    },
    "Tags" : {
      "type" : "array",
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    },
    "ProvisionedProductId" : {
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 50
    },
    "RecordId" : {
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 50
    },
    "CloudformationStackArn" : {
      "type" : "string",
      "minLength" : 1,
      "maxLength" : 256
    },
    "Outputs" : {
      "description" : "List of key-value pair outputs.",
      "type" : "object",
      "patternProperties" : {
        "^[A-Za-z0-9]{1,64}$" : {
          "$ref" : "#/definitions/OutputType"
        }
      },
      "additionalProperties" : False,
      "maxProperties" : 100
    }
  },
  "additionalProperties" : False,
  "readOnlyProperties" : [ "/properties/RecordId", "/properties/CloudformationStackArn", "/properties/Outputs", "/properties/ProvisionedProductId" ],
  "createOnlyProperties" : [ "/properties/NotificationArns", "/properties/ProvisionedProductName" ],
  "primaryIdentifier" : [ "/properties/ProvisionedProductId" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "servicecatalog:provisionProduct", "cloudformation:CreateStack" ],
      "timeoutInMinutes" : 720
    },
    "read" : {
      "permissions" : [ "servicecatalog:describeProvisionedProduct", "cloudformation:ListStacks" ]
    },
    "update" : {
      "permissions" : [ "servicecatalog:updateProvisionedProduct", "cloudformation:UpdateStack" ],
      "timeoutInMinutes" : 720
    },
    "delete" : {
      "permissions" : [ "servicecatalog:terminateProvisionedProduct", "servicecatalog:describeRecord", "cloudformation:DeleteStack" ]
    }
  }
}