SCHEMA = {
  "typeName" : "AWS::InspectorV2::Filter",
  "description" : "Inspector Filter resource schema",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-inspector.git",
  "definitions" : {
    "StringComparison" : {
      "type" : "string",
      "enum" : [ "EQUALS", "PREFIX", "NOT_EQUALS" ]
    },
    "StringInput" : {
      "type" : "string",
      "maxLength" : 1024,
      "minLength" : 1
    },
    "StringFilter" : {
      "type" : "object",
      "required" : [ "Comparison", "Value" ],
      "properties" : {
        "Comparison" : {
          "$ref" : "#/definitions/StringComparison"
        },
        "Value" : {
          "$ref" : "#/definitions/StringInput"
        }
      },
      "additionalProperties" : False
    },
    "StringFilterList" : {
      "type" : "array",
      "items" : {
        "$ref" : "#/definitions/StringFilter"
      },
      "insertionOrder" : False,
      "maxItems" : 10,
      "minItems" : 1
    },
    "Timestamp" : {
      "type" : "integer",
      "format" : "int64"
    },
    "DateFilter" : {
      "type" : "object",
      "properties" : {
        "EndInclusive" : {
          "$ref" : "#/definitions/Timestamp"
        },
        "StartInclusive" : {
          "$ref" : "#/definitions/Timestamp"
        }
      },
      "additionalProperties" : False
    },
    "DateFilterList" : {
      "type" : "array",
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/DateFilter"
      },
      "maxItems" : 10,
      "minItems" : 1
    },
    "Port" : {
      "type" : "integer",
      "maximum" : 65535,
      "minimum" : 0
    },
    "PortRangeFilter" : {
      "type" : "object",
      "properties" : {
        "BeginInclusive" : {
          "$ref" : "#/definitions/Port"
        },
        "EndInclusive" : {
          "$ref" : "#/definitions/Port"
        }
      },
      "additionalProperties" : False
    },
    "PortRangeFilterList" : {
      "type" : "array",
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/PortRangeFilter"
      },
      "maxItems" : 10,
      "minItems" : 1
    },
    "NumberFilter" : {
      "type" : "object",
      "properties" : {
        "LowerInclusive" : {
          "type" : "number"
        },
        "UpperInclusive" : {
          "type" : "number"
        }
      },
      "additionalProperties" : False
    },
    "NumberFilterList" : {
      "type" : "array",
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/NumberFilter"
      },
      "maxItems" : 10,
      "minItems" : 1
    },
    "MapComparison" : {
      "type" : "string",
      "enum" : [ "EQUALS" ]
    },
    "MapFilter" : {
      "type" : "object",
      "required" : [ "Comparison" ],
      "properties" : {
        "Comparison" : {
          "$ref" : "#/definitions/MapComparison"
        },
        "Key" : {
          "$ref" : "#/definitions/MapKey"
        },
        "Value" : {
          "$ref" : "#/definitions/MapValue"
        }
      },
      "additionalProperties" : False
    },
    "MapFilterList" : {
      "type" : "array",
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/MapFilter"
      },
      "maxItems" : 10,
      "minItems" : 1
    },
    "PackageFilter" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Architecture" : {
          "$ref" : "#/definitions/StringFilter"
        },
        "Epoch" : {
          "$ref" : "#/definitions/NumberFilter"
        },
        "Name" : {
          "$ref" : "#/definitions/StringFilter"
        },
        "Release" : {
          "$ref" : "#/definitions/StringFilter"
        },
        "SourceLayerHash" : {
          "$ref" : "#/definitions/StringFilter"
        },
        "Version" : {
          "$ref" : "#/definitions/StringFilter"
        }
      }
    },
    "PackageFilterList" : {
      "type" : "array",
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/PackageFilter"
      },
      "maxItems" : 10,
      "minItems" : 1
    },
    "FilterCriteria" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "AwsAccountId" : {
          "$ref" : "#/definitions/StringFilterList"
        },
        "ComponentId" : {
          "$ref" : "#/definitions/StringFilterList"
        },
        "ComponentType" : {
          "$ref" : "#/definitions/StringFilterList"
        },
        "Ec2InstanceImageId" : {
          "$ref" : "#/definitions/StringFilterList"
        },
        "Ec2InstanceSubnetId" : {
          "$ref" : "#/definitions/StringFilterList"
        },
        "Ec2InstanceVpcId" : {
          "$ref" : "#/definitions/StringFilterList"
        },
        "EcrImageArchitecture" : {
          "$ref" : "#/definitions/StringFilterList"
        },
        "EcrImageHash" : {
          "$ref" : "#/definitions/StringFilterList"
        },
        "EcrImageTags" : {
          "$ref" : "#/definitions/StringFilterList"
        },
        "EcrImagePushedAt" : {
          "$ref" : "#/definitions/DateFilterList"
        },
        "EcrImageRegistry" : {
          "$ref" : "#/definitions/StringFilterList"
        },
        "EcrImageRepositoryName" : {
          "$ref" : "#/definitions/StringFilterList"
        },
        "FindingArn" : {
          "$ref" : "#/definitions/StringFilterList"
        },
        "FindingStatus" : {
          "$ref" : "#/definitions/StringFilterList"
        },
        "FindingType" : {
          "$ref" : "#/definitions/StringFilterList"
        },
        "FirstObservedAt" : {
          "$ref" : "#/definitions/DateFilterList"
        },
        "InspectorScore" : {
          "$ref" : "#/definitions/NumberFilterList"
        },
        "LastObservedAt" : {
          "$ref" : "#/definitions/DateFilterList"
        },
        "NetworkProtocol" : {
          "$ref" : "#/definitions/StringFilterList"
        },
        "PortRange" : {
          "$ref" : "#/definitions/PortRangeFilterList"
        },
        "RelatedVulnerabilities" : {
          "$ref" : "#/definitions/StringFilterList"
        },
        "ResourceId" : {
          "$ref" : "#/definitions/StringFilterList"
        },
        "ResourceTags" : {
          "$ref" : "#/definitions/MapFilterList"
        },
        "ResourceType" : {
          "$ref" : "#/definitions/StringFilterList"
        },
        "Severity" : {
          "$ref" : "#/definitions/StringFilterList"
        },
        "Title" : {
          "$ref" : "#/definitions/StringFilterList"
        },
        "UpdatedAt" : {
          "$ref" : "#/definitions/DateFilterList"
        },
        "VendorSeverity" : {
          "$ref" : "#/definitions/StringFilterList"
        },
        "VulnerabilityId" : {
          "$ref" : "#/definitions/StringFilterList"
        },
        "VulnerabilitySource" : {
          "$ref" : "#/definitions/StringFilterList"
        },
        "VulnerablePackages" : {
          "$ref" : "#/definitions/PackageFilterList"
        }
      }
    },
    "FilterAction" : {
      "type" : "string",
      "enum" : [ "NONE", "SUPPRESS" ]
    },
    "MapKey" : {
      "type" : "string",
      "maxLength" : 128,
      "minLength" : 1
    },
    "MapValue" : {
      "type" : "string",
      "maxLength" : 256,
      "minLength" : 0
    }
  },
  "properties" : {
    "Name" : {
      "description" : "Findings filter name.",
      "type" : "string",
      "maxLength" : 128,
      "minLength" : 1
    },
    "Description" : {
      "description" : "Findings filter description.",
      "type" : "string",
      "maxLength" : 512,
      "minLength" : 1
    },
    "FilterCriteria" : {
      "description" : "Findings filter criteria.",
      "$ref" : "#/definitions/FilterCriteria"
    },
    "FilterAction" : {
      "description" : "Findings filter action.",
      "$ref" : "#/definitions/FilterAction"
    },
    "Arn" : {
      "description" : "Findings filter ARN.",
      "type" : "string",
      "maxLength" : 128,
      "minLength" : 1
    }
  },
  "tagging" : {
    "taggable" : False
  },
  "required" : [ "Name", "FilterCriteria", "FilterAction" ],
  "readOnlyProperties" : [ "/properties/Arn" ],
  "additionalProperties" : False,
  "primaryIdentifier" : [ "/properties/Arn" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "inspector2:CreateFilter", "inspector2:ListFilters" ]
    },
    "read" : {
      "permissions" : [ "inspector2:ListFilters" ]
    },
    "update" : {
      "permissions" : [ "inspector2:ListFilters", "inspector2:UpdateFilter" ]
    },
    "delete" : {
      "permissions" : [ "inspector2:DeleteFilter", "inspector2:ListFilters" ]
    },
    "list" : {
      "permissions" : [ "inspector2:ListFilters" ]
    }
  }
}