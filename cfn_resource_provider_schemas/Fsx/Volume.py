SCHEMA = {
  "typeName" : "AWS::FSx::Volume",
  "description" : "Resource Type definition for AWS::FSx::Volume",
  "additionalProperties" : False,
  "properties" : {
    "OpenZFSConfiguration" : {
      "$ref" : "#/definitions/OpenZFSConfiguration"
    },
    "ResourceARN" : {
      "type" : "string"
    },
    "VolumeId" : {
      "type" : "string"
    },
    "VolumeType" : {
      "type" : "string"
    },
    "BackupId" : {
      "type" : "string"
    },
    "OntapConfiguration" : {
      "$ref" : "#/definitions/OntapConfiguration"
    },
    "UUID" : {
      "type" : "string"
    },
    "Tags" : {
      "type" : "array",
      "uniqueItems" : False,
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    },
    "Name" : {
      "type" : "string"
    }
  },
  "definitions" : {
    "TieringPolicy" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "CoolingPeriod" : {
          "type" : "integer"
        },
        "Name" : {
          "type" : "string"
        }
      }
    },
    "SnaplockRetentionPeriod" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "MinimumRetention" : {
          "$ref" : "#/definitions/RetentionPeriod"
        },
        "DefaultRetention" : {
          "$ref" : "#/definitions/RetentionPeriod"
        },
        "MaximumRetention" : {
          "$ref" : "#/definitions/RetentionPeriod"
        }
      },
      "required" : [ "DefaultRetention", "MaximumRetention", "MinimumRetention" ]
    },
    "OntapConfiguration" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "JunctionPath" : {
          "type" : "string"
        },
        "StorageVirtualMachineId" : {
          "type" : "string"
        },
        "TieringPolicy" : {
          "$ref" : "#/definitions/TieringPolicy"
        },
        "SizeInMegabytes" : {
          "type" : "string"
        },
        "VolumeStyle" : {
          "type" : "string"
        },
        "SizeInBytes" : {
          "type" : "string"
        },
        "SecurityStyle" : {
          "type" : "string"
        },
        "SnaplockConfiguration" : {
          "$ref" : "#/definitions/SnaplockConfiguration"
        },
        "AggregateConfiguration" : {
          "$ref" : "#/definitions/AggregateConfiguration"
        },
        "SnapshotPolicy" : {
          "type" : "string"
        },
        "StorageEfficiencyEnabled" : {
          "type" : "string"
        },
        "CopyTagsToBackups" : {
          "type" : "string"
        },
        "OntapVolumeType" : {
          "type" : "string"
        }
      },
      "required" : [ "StorageVirtualMachineId" ]
    },
    "RetentionPeriod" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Value" : {
          "type" : "integer"
        },
        "Type" : {
          "type" : "string"
        }
      },
      "required" : [ "Type" ]
    },
    "SnaplockConfiguration" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "AuditLogVolume" : {
          "type" : "string"
        },
        "VolumeAppendModeEnabled" : {
          "type" : "string"
        },
        "AutocommitPeriod" : {
          "$ref" : "#/definitions/AutocommitPeriod"
        },
        "RetentionPeriod" : {
          "$ref" : "#/definitions/SnaplockRetentionPeriod"
        },
        "PrivilegedDelete" : {
          "type" : "string"
        },
        "SnaplockType" : {
          "type" : "string"
        }
      },
      "required" : [ "SnaplockType" ]
    },
    "OriginSnapshot" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "SnapshotARN" : {
          "type" : "string"
        },
        "CopyStrategy" : {
          "type" : "string"
        }
      },
      "required" : [ "CopyStrategy", "SnapshotARN" ]
    },
    "OpenZFSConfiguration" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "ReadOnly" : {
          "type" : "boolean"
        },
        "Options" : {
          "type" : "array",
          "uniqueItems" : False,
          "items" : {
            "type" : "string"
          }
        },
        "DataCompressionType" : {
          "type" : "string"
        },
        "NfsExports" : {
          "type" : "array",
          "uniqueItems" : False,
          "items" : {
            "$ref" : "#/definitions/NfsExports"
          }
        },
        "StorageCapacityQuotaGiB" : {
          "type" : "integer"
        },
        "CopyTagsToSnapshots" : {
          "type" : "boolean"
        },
        "ParentVolumeId" : {
          "type" : "string"
        },
        "StorageCapacityReservationGiB" : {
          "type" : "integer"
        },
        "RecordSizeKiB" : {
          "type" : "integer"
        },
        "OriginSnapshot" : {
          "$ref" : "#/definitions/OriginSnapshot"
        },
        "UserAndGroupQuotas" : {
          "type" : "array",
          "uniqueItems" : False,
          "items" : {
            "$ref" : "#/definitions/UserAndGroupQuotas"
          }
        }
      },
      "required" : [ "ParentVolumeId" ]
    },
    "AggregateConfiguration" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Aggregates" : {
          "type" : "array",
          "uniqueItems" : False,
          "items" : {
            "type" : "string"
          }
        },
        "ConstituentsPerAggregate" : {
          "type" : "integer"
        }
      }
    },
    "NfsExports" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "ClientConfigurations" : {
          "type" : "array",
          "uniqueItems" : False,
          "items" : {
            "$ref" : "#/definitions/ClientConfigurations"
          }
        }
      },
      "required" : [ "ClientConfigurations" ]
    },
    "ClientConfigurations" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Clients" : {
          "type" : "string"
        },
        "Options" : {
          "type" : "array",
          "uniqueItems" : False,
          "items" : {
            "type" : "string"
          }
        }
      },
      "required" : [ "Options", "Clients" ]
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
    "AutocommitPeriod" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Value" : {
          "type" : "integer"
        },
        "Type" : {
          "type" : "string"
        }
      },
      "required" : [ "Type" ]
    },
    "UserAndGroupQuotas" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Type" : {
          "type" : "string"
        },
        "Id" : {
          "type" : "integer"
        },
        "StorageCapacityQuotaGiB" : {
          "type" : "integer"
        }
      },
      "required" : [ "Type", "Id", "StorageCapacityQuotaGiB" ]
    }
  },
  "required" : [ "Name" ],
  "createOnlyProperties" : [ "/properties/BackupId", "/properties/VolumeType" ],
  "primaryIdentifier" : [ "/properties/VolumeId" ],
  "readOnlyProperties" : [ "/properties/ResourceARN", "/properties/VolumeId", "/properties/UUID" ]
}