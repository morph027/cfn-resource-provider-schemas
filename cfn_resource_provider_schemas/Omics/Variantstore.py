SCHEMA = {
  "typeName" : "AWS::Omics::VariantStore",
  "description" : "Definition of AWS::Omics::VariantStore Resource Type",
  "definitions" : {
    "EncryptionType" : {
      "type" : "string",
      "enum" : [ "KMS" ]
    },
    "ReferenceItem" : {
      "type" : "object",
      "properties" : {
        "ReferenceArn" : {
          "type" : "string",
          "maxLength" : 127,
          "minLength" : 1,
          "pattern" : "^arn:.+$"
        }
      },
      "required" : [ "ReferenceArn" ],
      "additionalProperties" : False
    },
    "SseConfig" : {
      "type" : "object",
      "properties" : {
        "Type" : {
          "$ref" : "#/definitions/EncryptionType"
        },
        "KeyArn" : {
          "type" : "string",
          "maxLength" : 2048,
          "minLength" : 20,
          "pattern" : "arn:([^:\n]*):([^:\n]*):([^:\n]*):([0-9]{12}):([^:\n]*)"
        }
      },
      "required" : [ "Type" ],
      "additionalProperties" : False
    },
    "StoreStatus" : {
      "type" : "string",
      "enum" : [ "CREATING", "UPDATING", "DELETING", "ACTIVE", "FAILED" ]
    },
    "TagMap" : {
      "type" : "object",
      "patternProperties" : {
        ".+" : {
          "type" : "string",
          "maxLength" : 256,
          "minLength" : 0
        }
      },
      "additionalProperties" : False
    }
  },
  "properties" : {
    "CreationTime" : {
      "type" : "string",
      "format" : "date-time"
    },
    "Description" : {
      "type" : "string",
      "maxLength" : 500,
      "minLength" : 0
    },
    "Id" : {
      "type" : "string",
      "pattern" : "^[a-f0-9]{12}$"
    },
    "Name" : {
      "type" : "string",
      "pattern" : "^([a-z]){1}([a-z0-9_]){2,254}"
    },
    "Reference" : {
      "$ref" : "#/definitions/ReferenceItem"
    },
    "SseConfig" : {
      "$ref" : "#/definitions/SseConfig"
    },
    "Status" : {
      "$ref" : "#/definitions/StoreStatus"
    },
    "StatusMessage" : {
      "type" : "string",
      "maxLength" : 1000,
      "minLength" : 0
    },
    "StoreArn" : {
      "type" : "string",
      "maxLength" : 2048,
      "minLength" : 20,
      "pattern" : "^arn:([^:\n]*):([^:\n]*):([^:\n]*):([0-9]{12}):([^:\n]*)$"
    },
    "StoreSizeBytes" : {
      "type" : "number"
    },
    "Tags" : {
      "$ref" : "#/definitions/TagMap"
    },
    "UpdateTime" : {
      "type" : "string",
      "format" : "date-time"
    }
  },
  "required" : [ "Name", "Reference" ],
  "readOnlyProperties" : [ "/properties/CreationTime", "/properties/Id", "/properties/Status", "/properties/StatusMessage", "/properties/StoreArn", "/properties/StoreSizeBytes", "/properties/UpdateTime" ],
  "createOnlyProperties" : [ "/properties/Name", "/properties/Reference", "/properties/SseConfig", "/properties/Tags" ],
  "primaryIdentifier" : [ "/properties/Name" ],
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : False,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "omics:TagResource", "omics:UntagResource", "omics:ListTagsForResource" ]
  },
  "handlers" : {
    "create" : {
      "permissions" : [ "omics:CreateVariantStore", "omics:TagResource", "kms:DescribeKey", "kms:GenerateDataKey", "kms:CreateGrant", "ram:AcceptResourceShareInvitation", "ram:GetResourceShareInvitations", "omics:GetVariantStore" ]
    },
    "read" : {
      "permissions" : [ "omics:GetVariantStore" ]
    },
    "update" : {
      "permissions" : [ "omics:UpdateVariantStore", "omics:TagResource", "omics:UntagResource", "omics:ListTagsForResource", "omics:GetVariantStore" ]
    },
    "delete" : {
      "permissions" : [ "omics:DeleteVariantStore", "omics:ListVariantStores" ]
    },
    "list" : {
      "permissions" : [ "omics:ListVariantStores" ]
    }
  },
  "additionalProperties" : False
}