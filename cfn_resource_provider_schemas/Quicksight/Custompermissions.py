SCHEMA = {
  "typeName" : "AWS::QuickSight::CustomPermissions",
  "description" : "Definition of the AWS::QuickSight::CustomPermissions Resource Type.",
  "definitions" : {
    "Capabilities" : {
      "type" : "object",
      "properties" : {
        "ExportToCsv" : {
          "$ref" : "#/definitions/CapabilityState"
        },
        "ExportToExcel" : {
          "$ref" : "#/definitions/CapabilityState"
        },
        "CreateAndUpdateThemes" : {
          "$ref" : "#/definitions/CapabilityState"
        },
        "AddOrRunAnomalyDetectionForAnalyses" : {
          "$ref" : "#/definitions/CapabilityState"
        },
        "ShareAnalyses" : {
          "$ref" : "#/definitions/CapabilityState"
        },
        "CreateAndUpdateDatasets" : {
          "$ref" : "#/definitions/CapabilityState"
        },
        "ShareDatasets" : {
          "$ref" : "#/definitions/CapabilityState"
        },
        "SubscribeDashboardEmailReports" : {
          "$ref" : "#/definitions/CapabilityState"
        },
        "CreateAndUpdateDashboardEmailReports" : {
          "$ref" : "#/definitions/CapabilityState"
        },
        "ShareDashboards" : {
          "$ref" : "#/definitions/CapabilityState"
        },
        "CreateAndUpdateThresholdAlerts" : {
          "$ref" : "#/definitions/CapabilityState"
        },
        "RenameSharedFolders" : {
          "$ref" : "#/definitions/CapabilityState"
        },
        "CreateSharedFolders" : {
          "$ref" : "#/definitions/CapabilityState"
        },
        "CreateAndUpdateDataSources" : {
          "$ref" : "#/definitions/CapabilityState"
        },
        "ShareDataSources" : {
          "$ref" : "#/definitions/CapabilityState"
        },
        "ViewAccountSPICECapacity" : {
          "$ref" : "#/definitions/CapabilityState"
        },
        "CreateSPICEDataset" : {
          "$ref" : "#/definitions/CapabilityState"
        }
      },
      "additionalProperties" : False
    },
    "CapabilityState" : {
      "type" : "string",
      "enum" : [ "DENY" ]
    },
    "Tag" : {
      "type" : "object",
      "description" : "<p>The key or keys of the key-value pairs for the resource tag or tags assigned to the\n            resource.</p>",
      "properties" : {
        "Key" : {
          "type" : "string",
          "maxLength" : 128,
          "minLength" : 1,
          "description" : "<p>Tag key.</p>"
        },
        "Value" : {
          "type" : "string",
          "maxLength" : 256,
          "minLength" : 1,
          "description" : "<p>Tag value.</p>"
        }
      },
      "required" : [ "Key", "Value" ],
      "additionalProperties" : False
    }
  },
  "properties" : {
    "Arn" : {
      "type" : "string"
    },
    "AwsAccountId" : {
      "type" : "string",
      "maxLength" : 12,
      "minLength" : 12,
      "pattern" : "^[0-9]{12}$"
    },
    "Capabilities" : {
      "$ref" : "#/definitions/Capabilities"
    },
    "CustomPermissionsName" : {
      "type" : "string",
      "maxLength" : 64,
      "minLength" : 1,
      "pattern" : "^[a-zA-Z0-9+=,.@_-]+$"
    },
    "Tags" : {
      "type" : "array",
      "items" : {
        "$ref" : "#/definitions/Tag"
      },
      "maxItems" : 200,
      "minItems" : 1
    }
  },
  "readOnlyProperties" : [ "/properties/Arn" ],
  "createOnlyProperties" : [ "/properties/AwsAccountId", "/properties/CustomPermissionsName" ],
  "primaryIdentifier" : [ "/properties/AwsAccountId", "/properties/CustomPermissionsName" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "quicksight:CreateCustomPermissions", "quicksight:TagResource" ]
    },
    "read" : {
      "permissions" : [ "quicksight:DescribeCustomPermissions", "quicksight:ListTagsForResource" ]
    },
    "update" : {
      "permissions" : [ "quicksight:UpdateCustomPermissions", "quicksight:TagResource", "quicksight:UntagResource", "quicksight:ListTagsForResource" ]
    },
    "delete" : {
      "permissions" : [ "quicksight:DeleteCustomPermissions" ]
    },
    "list" : {
      "permissions" : [ "quicksight:ListCustomPermissions" ]
    }
  },
  "additionalProperties" : False,
  "required" : [ "AwsAccountId", "CustomPermissionsName" ],
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : False,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "quicksight:TagResource", "quicksight:UntagResource", "quicksight:ListTagsForResource" ]
  }
}