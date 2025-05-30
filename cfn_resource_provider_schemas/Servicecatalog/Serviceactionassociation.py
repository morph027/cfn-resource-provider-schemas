SCHEMA = {
  "typeName" : "AWS::ServiceCatalog::ServiceActionAssociation",
  "description" : "Resource Schema for AWS::ServiceCatalog::ServiceActionAssociation",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-servicecatalog",
  "properties" : {
    "ProductId" : {
      "type" : "string",
      "pattern" : "^[a-zA-Z0-9][a-zA-Z0-9_-]{1,99}\\Z",
      "minLength" : 1,
      "maxLength" : 100
    },
    "ProvisioningArtifactId" : {
      "type" : "string",
      "pattern" : "^[a-zA-Z0-9][a-zA-Z0-9_-]{1,99}\\Z",
      "minLength" : 1,
      "maxLength" : 100
    },
    "ServiceActionId" : {
      "type" : "string",
      "pattern" : "^[a-zA-Z0-9][a-zA-Z0-9_-]{1,99}\\Z",
      "minLength" : 1,
      "maxLength" : 100
    }
  },
  "additionalProperties" : False,
  "required" : [ "ProductId", "ProvisioningArtifactId", "ServiceActionId" ],
  "createOnlyProperties" : [ "/properties/ProductId", "/properties/ProvisioningArtifactId", "/properties/ServiceActionId" ],
  "primaryIdentifier" : [ "/properties/ProductId", "/properties/ProvisioningArtifactId", "/properties/ServiceActionId" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "servicecatalog:AssociateServiceActionWithProvisioningArtifact", "servicecatalog:ListServiceActionsForProvisioningArtifact" ]
    },
    "read" : {
      "permissions" : [ "servicecatalog:ListServiceActionsForProvisioningArtifact" ]
    },
    "delete" : {
      "permissions" : [ "servicecatalog:DisassociateServiceActionFromProvisioningArtifact", "servicecatalog:ListServiceActionsForProvisioningArtifact" ]
    },
    "list" : {
      "handlerSchema" : {
        "properties" : {
          "ProductId" : {
            "$ref" : "resource-schema.json#/properties/ProductId"
          },
          "ProvisioningArtifactId" : {
            "$ref" : "resource-schema.json#/properties/ProvisioningArtifactId"
          }
        },
        "required" : [ "ProductId", "ProvisioningArtifactId" ]
      },
      "permissions" : [ "servicecatalog:ListServiceActionsForProvisioningArtifact" ]
    }
  }
}