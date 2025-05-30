SCHEMA = {
  "typeName" : "AWS::IoTFleetWise::DecoderManifest",
  "description" : "Definition of AWS::IoTFleetWise::DecoderManifest Resource Type",
  "definitions" : {
    "CanInterface" : {
      "type" : "object",
      "properties" : {
        "Name" : {
          "type" : "string",
          "maxLength" : 100,
          "minLength" : 1
        },
        "ProtocolName" : {
          "type" : "string",
          "maxLength" : 50,
          "minLength" : 1
        },
        "ProtocolVersion" : {
          "type" : "string",
          "maxLength" : 50,
          "minLength" : 1
        }
      },
      "required" : [ "Name" ],
      "additionalProperties" : False
    },
    "CanSignal" : {
      "type" : "object",
      "properties" : {
        "MessageId" : {
          "type" : [ "integer", "string" ]
        },
        "IsBigEndian" : {
          "type" : [ "boolean", "string" ]
        },
        "IsSigned" : {
          "type" : [ "boolean", "string" ]
        },
        "StartBit" : {
          "type" : [ "integer", "string" ]
        },
        "Offset" : {
          "type" : [ "number", "string" ]
        },
        "Factor" : {
          "type" : [ "number", "string" ]
        },
        "Length" : {
          "type" : [ "integer", "string" ]
        },
        "Name" : {
          "type" : "string",
          "maxLength" : 100,
          "minLength" : 1
        },
        "SignalValueType" : {
          "$ref" : "#/definitions/SignalValueType"
        }
      },
      "required" : [ "Factor", "IsBigEndian", "IsSigned", "Length", "MessageId", "Offset", "StartBit" ],
      "additionalProperties" : False
    },
    "ManifestStatus" : {
      "type" : "string",
      "enum" : [ "ACTIVE", "DRAFT" ],
      "default" : "DRAFT"
    },
    "CanNetworkInterface" : {
      "type" : "object",
      "properties" : {
        "InterfaceId" : {
          "type" : "string",
          "maxLength" : 50,
          "minLength" : 1
        },
        "Type" : {
          "type" : "string",
          "enum" : [ "CAN_INTERFACE" ]
        },
        "CanInterface" : {
          "$ref" : "#/definitions/CanInterface"
        }
      },
      "required" : [ "InterfaceId", "Type", "CanInterface" ],
      "additionalProperties" : False
    },
    "ObdNetworkInterface" : {
      "type" : "object",
      "properties" : {
        "InterfaceId" : {
          "type" : "string",
          "maxLength" : 50,
          "minLength" : 1
        },
        "Type" : {
          "type" : "string",
          "enum" : [ "OBD_INTERFACE" ]
        },
        "ObdInterface" : {
          "$ref" : "#/definitions/ObdInterface"
        }
      },
      "required" : [ "InterfaceId", "Type", "ObdInterface" ],
      "additionalProperties" : False
    },
    "ObdInterface" : {
      "type" : "object",
      "properties" : {
        "Name" : {
          "type" : "string",
          "maxLength" : 100,
          "minLength" : 1
        },
        "RequestMessageId" : {
          "type" : [ "integer", "string" ]
        },
        "ObdStandard" : {
          "type" : "string",
          "maxLength" : 50,
          "minLength" : 1
        },
        "PidRequestIntervalSeconds" : {
          "type" : [ "integer", "string" ]
        },
        "DtcRequestIntervalSeconds" : {
          "type" : [ "integer", "string" ]
        },
        "UseExtendedIds" : {
          "type" : [ "boolean", "string" ]
        },
        "HasTransmissionEcu" : {
          "type" : [ "boolean", "string" ]
        }
      },
      "required" : [ "Name", "RequestMessageId" ],
      "additionalProperties" : False
    },
    "ObdSignal" : {
      "type" : "object",
      "properties" : {
        "PidResponseLength" : {
          "type" : [ "integer", "string" ]
        },
        "ServiceMode" : {
          "type" : [ "integer", "string" ]
        },
        "Pid" : {
          "type" : [ "integer", "string" ]
        },
        "Scaling" : {
          "type" : [ "number", "string" ]
        },
        "Offset" : {
          "type" : [ "number", "string" ]
        },
        "StartByte" : {
          "type" : [ "integer", "string" ]
        },
        "ByteLength" : {
          "type" : [ "integer", "string" ]
        },
        "BitRightShift" : {
          "type" : [ "integer", "string" ]
        },
        "BitMaskLength" : {
          "type" : [ "integer", "string" ]
        },
        "IsSigned" : {
          "type" : [ "boolean", "string" ]
        },
        "SignalValueType" : {
          "$ref" : "#/definitions/SignalValueType"
        }
      },
      "required" : [ "ByteLength", "Offset", "Pid", "PidResponseLength", "Scaling", "ServiceMode", "StartByte" ],
      "additionalProperties" : False
    },
    "CanSignalDecoder" : {
      "type" : "object",
      "properties" : {
        "FullyQualifiedName" : {
          "type" : "string",
          "maxLength" : 150,
          "minLength" : 1
        },
        "Type" : {
          "type" : "string",
          "enum" : [ "CAN_SIGNAL" ]
        },
        "InterfaceId" : {
          "type" : "string",
          "maxLength" : 50,
          "minLength" : 1
        },
        "CanSignal" : {
          "$ref" : "#/definitions/CanSignal"
        }
      },
      "required" : [ "FullyQualifiedName", "InterfaceId", "Type", "CanSignal" ],
      "additionalProperties" : False
    },
    "ObdSignalDecoder" : {
      "type" : "object",
      "properties" : {
        "FullyQualifiedName" : {
          "type" : "string",
          "maxLength" : 150,
          "minLength" : 1
        },
        "Type" : {
          "type" : "string",
          "enum" : [ "OBD_SIGNAL" ]
        },
        "InterfaceId" : {
          "type" : "string",
          "maxLength" : 50,
          "minLength" : 1
        },
        "ObdSignal" : {
          "$ref" : "#/definitions/ObdSignal"
        }
      },
      "required" : [ "FullyQualifiedName", "InterfaceId", "Type", "ObdSignal" ],
      "additionalProperties" : False
    },
    "SignalValueType" : {
      "type" : "string",
      "enum" : [ "INTEGER", "FLOATING_POINT" ]
    },
    "Tag" : {
      "type" : "object",
      "properties" : {
        "Key" : {
          "type" : "string",
          "maxLength" : 128,
          "minLength" : 1
        },
        "Value" : {
          "type" : "string",
          "maxLength" : 256,
          "minLength" : 0
        }
      },
      "required" : [ "Key", "Value" ],
      "additionalProperties" : False
    },
    "CustomDecodingNetworkInterface" : {
      "type" : "object",
      "properties" : {
        "InterfaceId" : {
          "type" : "string",
          "maxLength" : 50,
          "minLength" : 1
        },
        "Type" : {
          "type" : "string",
          "enum" : [ "CUSTOM_DECODING_INTERFACE" ]
        },
        "CustomDecodingInterface" : {
          "$ref" : "#/definitions/CustomDecodingInterface"
        }
      },
      "required" : [ "InterfaceId", "Type", "CustomDecodingInterface" ],
      "additionalProperties" : False
    },
    "CustomDecodingInterface" : {
      "type" : "object",
      "properties" : {
        "Name" : {
          "type" : "string",
          "maxLength" : 100,
          "minLength" : 1,
          "pattern" : "^[a-zA-Z\\d\\-_:]+$"
        }
      },
      "required" : [ "Name" ],
      "additionalProperties" : False
    },
    "CustomDecodingSignal" : {
      "type" : "object",
      "properties" : {
        "Id" : {
          "type" : "string",
          "maxLength" : 150,
          "minLength" : 1,
          "pattern" : "^(?!.*\\.\\.)[a-zA-Z0-9_\\-#:.]+$"
        }
      },
      "required" : [ "Id" ],
      "additionalProperties" : False
    },
    "CustomDecodingSignalDecoder" : {
      "type" : "object",
      "properties" : {
        "FullyQualifiedName" : {
          "type" : "string",
          "maxLength" : 150,
          "minLength" : 1
        },
        "Type" : {
          "type" : "string",
          "enum" : [ "CUSTOM_DECODING_SIGNAL" ]
        },
        "InterfaceId" : {
          "type" : "string",
          "maxLength" : 50,
          "minLength" : 1
        },
        "CustomDecodingSignal" : {
          "$ref" : "#/definitions/CustomDecodingSignal"
        }
      },
      "required" : [ "FullyQualifiedName", "InterfaceId", "Type", "CustomDecodingSignal" ],
      "additionalProperties" : False
    },
    "DefaultForUnmappedSignalsType" : {
      "type" : "string",
      "enum" : [ "CUSTOM_DECODING" ]
    }
  },
  "properties" : {
    "Arn" : {
      "type" : "string"
    },
    "CreationTime" : {
      "type" : "string",
      "format" : "date-time"
    },
    "Description" : {
      "type" : "string",
      "maxLength" : 2048,
      "minLength" : 1,
      "pattern" : "^[^\\u0000-\\u001F\\u007F]+$"
    },
    "LastModificationTime" : {
      "type" : "string",
      "format" : "date-time"
    },
    "ModelManifestArn" : {
      "type" : "string"
    },
    "Name" : {
      "type" : "string",
      "maxLength" : 100,
      "minLength" : 1,
      "pattern" : "^[a-zA-Z\\d\\-_:]+$"
    },
    "NetworkInterfaces" : {
      "insertionOrder" : False,
      "type" : "array",
      "items" : {
        "oneOf" : [ {
          "$ref" : "#/definitions/CanNetworkInterface"
        }, {
          "$ref" : "#/definitions/ObdNetworkInterface"
        }, {
          "$ref" : "#/definitions/CustomDecodingNetworkInterface"
        } ]
      },
      "maxItems" : 5000,
      "minItems" : 1
    },
    "SignalDecoders" : {
      "insertionOrder" : False,
      "type" : "array",
      "items" : {
        "oneOf" : [ {
          "$ref" : "#/definitions/CanSignalDecoder"
        }, {
          "$ref" : "#/definitions/ObdSignalDecoder"
        }, {
          "$ref" : "#/definitions/CustomDecodingSignalDecoder"
        } ]
      },
      "maxItems" : 5000,
      "minItems" : 1
    },
    "Status" : {
      "$ref" : "#/definitions/ManifestStatus"
    },
    "DefaultForUnmappedSignals" : {
      "$ref" : "#/definitions/DefaultForUnmappedSignalsType"
    },
    "Tags" : {
      "type" : "array",
      "items" : {
        "$ref" : "#/definitions/Tag"
      },
      "maxItems" : 50,
      "minItems" : 0,
      "insertionOrder" : False,
      "uniqueItems" : True
    }
  },
  "required" : [ "Name", "ModelManifestArn" ],
  "readOnlyProperties" : [ "/properties/Arn", "/properties/CreationTime", "/properties/LastModificationTime" ],
  "createOnlyProperties" : [ "/properties/Name", "/properties/ModelManifestArn" ],
  "writeOnlyProperties" : [ "/properties/DefaultForUnmappedSignals" ],
  "primaryIdentifier" : [ "/properties/Name" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "iotfleetwise:CreateDecoderManifest", "iotfleetwise:GetDecoderManifest", "iotfleetwise:UpdateDecoderManifest", "iotfleetwise:ListDecoderManifestSignals", "iotfleetwise:ListDecoderManifestNetworkInterfaces", "iotfleetwise:ListTagsForResource", "iotfleetwise:TagResource" ]
    },
    "read" : {
      "permissions" : [ "iotfleetwise:GetDecoderManifest", "iotfleetwise:ListDecoderManifestSignals", "iotfleetwise:ListDecoderManifestNetworkInterfaces", "iotfleetwise:ListTagsForResource" ]
    },
    "update" : {
      "permissions" : [ "iotfleetwise:UpdateDecoderManifest", "iotfleetwise:GetDecoderManifest", "iotfleetwise:ListDecoderManifestSignals", "iotfleetwise:ListDecoderManifestNetworkInterfaces", "iotfleetwise:ListTagsForResource", "iotfleetwise:TagResource", "iotfleetwise:UntagResource" ]
    },
    "delete" : {
      "permissions" : [ "iotfleetwise:DeleteDecoderManifest", "iotfleetwise:GetDecoderManifest" ]
    },
    "list" : {
      "permissions" : [ "iotfleetwise:ListDecoderManifests" ]
    }
  },
  "additionalProperties" : False,
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : True,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "iotfleetwise:UntagResource", "iotfleetwise:TagResource", "iotfleetwise:ListTagsForResource" ]
  }
}