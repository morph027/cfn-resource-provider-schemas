SCHEMA = {
  "typeName" : "AWS::Deadline::StorageProfile",
  "description" : "Definition of AWS::Deadline::StorageProfile Resource Type",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-deadline",
  "definitions" : {
    "FileSystemLocation" : {
      "type" : "object",
      "properties" : {
        "Name" : {
          "type" : "string",
          "maxLength" : 64,
          "minLength" : 1,
          "pattern" : "^[0-9A-Za-z ]*$"
        },
        "Path" : {
          "type" : "string",
          "maxLength" : 1024,
          "minLength" : 0
        },
        "Type" : {
          "$ref" : "#/definitions/FileSystemLocationType"
        }
      },
      "required" : [ "Name", "Path", "Type" ],
      "additionalProperties" : False
    },
    "FileSystemLocationType" : {
      "type" : "string",
      "enum" : [ "SHARED", "LOCAL" ]
    },
    "StorageProfileOperatingSystemFamily" : {
      "type" : "string",
      "enum" : [ "WINDOWS", "LINUX", "MACOS" ]
    }
  },
  "properties" : {
    "DisplayName" : {
      "type" : "string",
      "maxLength" : 100,
      "minLength" : 1
    },
    "FarmId" : {
      "type" : "string",
      "pattern" : "^farm-[0-9a-f]{32}$"
    },
    "FileSystemLocations" : {
      "type" : "array",
      "items" : {
        "$ref" : "#/definitions/FileSystemLocation"
      },
      "maxItems" : 20,
      "minItems" : 0
    },
    "OsFamily" : {
      "$ref" : "#/definitions/StorageProfileOperatingSystemFamily"
    },
    "StorageProfileId" : {
      "type" : "string",
      "pattern" : "^sp-[0-9a-f]{32}$"
    }
  },
  "required" : [ "DisplayName", "FarmId", "OsFamily" ],
  "readOnlyProperties" : [ "/properties/StorageProfileId" ],
  "createOnlyProperties" : [ "/properties/FarmId" ],
  "primaryIdentifier" : [ "/properties/FarmId", "/properties/StorageProfileId" ],
  "tagging" : {
    "taggable" : False,
    "tagOnCreate" : False,
    "tagUpdatable" : False,
    "cloudFormationSystemTags" : False
  },
  "handlers" : {
    "create" : {
      "permissions" : [ "deadline:CreateStorageProfile", "deadline:GetStorageProfile", "identitystore:ListGroupMembershipsForMember" ]
    },
    "read" : {
      "permissions" : [ "deadline:GetStorageProfile", "identitystore:ListGroupMembershipsForMember" ]
    },
    "update" : {
      "permissions" : [ "deadline:UpdateStorageProfile", "deadline:GetStorageProfile", "identitystore:ListGroupMembershipsForMember" ]
    },
    "delete" : {
      "permissions" : [ "deadline:DeleteStorageProfile", "deadline:GetStorageProfile", "identitystore:ListGroupMembershipsForMember" ]
    },
    "list" : {
      "handlerSchema" : {
        "properties" : {
          "FarmId" : {
            "$ref" : "resource-schema.json#/properties/FarmId"
          }
        },
        "required" : [ "FarmId" ]
      },
      "permissions" : [ "deadline:ListStorageProfiles", "identitystore:ListGroupMembershipsForMember" ]
    }
  },
  "additionalProperties" : False
}