SCHEMA = {
  "typeName" : "AWS::AppSync::SourceApiAssociation",
  "description" : "Resource Type definition for AWS::AppSync::SourceApiAssociation",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-appsync",
  "definitions" : {
    "SourceApiAssociationConfig" : {
      "properties" : {
        "MergeType" : {
          "description" : "Configuration of the merged behavior for the association. For example when it could be auto or has to be manual.",
          "type" : "string",
          "enum" : [ "AUTO_MERGE", "MANUAL_MERGE" ]
        }
      },
      "additionalProperties" : False
    }
  },
  "properties" : {
    "SourceApiIdentifier" : {
      "description" : "Identifier of the Source GraphQLApi to associate. It could be either GraphQLApi ApiId or ARN",
      "type" : "string"
    },
    "MergedApiIdentifier" : {
      "description" : "Identifier of the Merged GraphQLApi to associate. It could be either GraphQLApi ApiId or ARN",
      "type" : "string"
    },
    "Description" : {
      "description" : "Description of the SourceApiAssociation.",
      "type" : "string"
    },
    "SourceApiAssociationConfig" : {
      "description" : "Customized configuration for SourceApiAssociation.",
      "$ref" : "#/definitions/SourceApiAssociationConfig"
    },
    "AssociationId" : {
      "description" : "Id of the SourceApiAssociation.",
      "type" : "string"
    },
    "AssociationArn" : {
      "description" : "ARN of the SourceApiAssociation.",
      "type" : "string"
    },
    "SourceApiId" : {
      "description" : "GraphQLApiId of the source API in the association.",
      "type" : "string"
    },
    "SourceApiArn" : {
      "description" : "ARN of the source API in the association.",
      "type" : "string",
      "pattern" : "^arn:aws(-(cn|us-gov))?:[a-z-]+:(([a-z]+-)+[0-9])?:([0-9]{12})?:[^.]+$"
    },
    "MergedApiId" : {
      "description" : "GraphQLApiId of the Merged API in the association.",
      "type" : "string"
    },
    "MergedApiArn" : {
      "description" : "ARN of the Merged API in the association.",
      "type" : "string",
      "pattern" : "^arn:aws(-(cn|us-gov))?:[a-z-]+:(([a-z]+-)+[0-9])?:([0-9]{12})?:[^.]+$"
    },
    "SourceApiAssociationStatus" : {
      "description" : "Current status of SourceApiAssociation.",
      "type" : "string",
      "enum" : [ "MERGE_SCHEDULED", "MERGE_FAILED", "MERGE_SUCCESS", "MERGE_IN_PROGRESS", "AUTO_MERGE_SCHEDULE_FAILED", "DELETION_SCHEDULED", "DELETION_IN_PROGRESS", "DELETION_FAILED" ]
    },
    "SourceApiAssociationStatusDetail" : {
      "description" : "Current SourceApiAssociation status details.",
      "type" : "string"
    },
    "LastSuccessfulMergeDate" : {
      "description" : "Date of last schema successful merge.",
      "type" : "string",
      "format" : "date-time"
    }
  },
  "additionalProperties" : False,
  "readOnlyProperties" : [ "/properties/AssociationId", "/properties/AssociationArn", "/properties/SourceApiId", "/properties/SourceApiArn", "/properties/MergedApiId", "/properties/MergedApiArn", "/properties/SourceApiAssociationStatus", "/properties/SourceApiAssociationStatusDetail", "/properties/LastSuccessfulMergeDate" ],
  "writeOnlyProperties" : [ "/properties/SourceApiIdentifier", "/properties/MergedApiIdentifier" ],
  "createOnlyProperties" : [ "/properties/SourceApiIdentifier", "/properties/MergedApiIdentifier" ],
  "primaryIdentifier" : [ "/properties/AssociationArn" ],
  "additionalIdentifiers" : [ [ "/properties/SourceApiIdentifier", "/properties/MergedApiIdentifier" ] ],
  "tagging" : {
    "taggable" : False,
    "tagOnCreate" : False,
    "tagUpdatable" : False,
    "cloudFormationSystemTags" : False
  },
  "handlers" : {
    "create" : {
      "permissions" : [ "appsync:AssociateSourceGraphqlApi", "appsync:AssociateMergedGraphqlApi", "appsync:GetSourceApiAssociation" ]
    },
    "read" : {
      "permissions" : [ "appsync:GetSourceApiAssociation", "appsync:ListSourceApiAssociations" ]
    },
    "update" : {
      "permissions" : [ "appsync:GetSourceApiAssociation", "appsync:UpdateSourceApiAssociation", "appsync:GetSourceApiAssociation" ]
    },
    "delete" : {
      "permissions" : [ "appsync:GetSourceApiAssociation", "appsync:DisassociateSourceGraphqlApi", "appsync:DisassociateMergedGraphqlApi", "appsync:ListSourceApiAssociations" ]
    },
    "list" : {
      "handlerSchema" : {
        "properties" : {
          "SourceApiIdentifier" : {
            "$ref" : "resource-schema.json#/properties/SourceApiIdentifier"
          },
          "MergedApiIdentifier" : {
            "$ref" : "resource-schema.json#/properties/MergedApiIdentifier"
          }
        },
        "required" : [ "SourceApiIdentifier", "MergedApiIdentifier" ]
      },
      "permissions" : [ "appsync:ListSourceApiAssociations" ]
    }
  }
}