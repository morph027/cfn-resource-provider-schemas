SCHEMA = {
  "typeName" : "AWS::SageMaker::Device",
  "description" : "Resource schema for AWS::SageMaker::Device",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-resource-providers-sagemaker-edge.git",
  "definitions" : {
    "Device" : {
      "description" : "Edge device you want to create",
      "type" : "object",
      "properties" : {
        "Description" : {
          "description" : "Description of the device",
          "type" : "string",
          "pattern" : "[\\S\\s]+",
          "minLength" : 1,
          "maxLength" : 40
        },
        "DeviceName" : {
          "description" : "The name of the device",
          "type" : "string",
          "pattern" : "^[a-zA-Z0-9](-*[a-zA-Z0-9])*$",
          "minLength" : 1,
          "maxLength" : 63
        },
        "IotThingName" : {
          "description" : "AWS Internet of Things (IoT) object name.",
          "type" : "string",
          "pattern" : "[a-zA-Z0-9:_-]+",
          "maxLength" : 128
        }
      },
      "required" : [ "DeviceName" ],
      "additionalProperties" : False
    },
    "Tag" : {
      "type" : "object",
      "properties" : {
        "Key" : {
          "description" : "The key name of the tag. You can specify a value that is 1 to 127 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -. ",
          "type" : "string",
          "pattern" : "^((?!aws:)[\\p{L}\\p{Z}\\p{N}_.:/=+\\-@]*)$",
          "minLength" : 1,
          "maxLength" : 128
        },
        "Value" : {
          "description" : "The key value of the tag. You can specify a value that is 1 to 127 Unicode characters in length and cannot be prefixed with aws:. You can use any of the following characters: the set of Unicode letters, digits, whitespace, _, ., /, =, +, and -. ",
          "type" : "string",
          "pattern" : "^([\\p{L}\\p{Z}\\p{N}_.:/=+\\-@]*)$",
          "minLength" : 0,
          "maxLength" : 256
        }
      },
      "required" : [ "Key", "Value" ],
      "additionalProperties" : False
    }
  },
  "properties" : {
    "DeviceFleetName" : {
      "description" : "The name of the edge device fleet",
      "type" : "string",
      "pattern" : "^[a-zA-Z0-9](-*_*[a-zA-Z0-9])*$",
      "minLength" : 1,
      "maxLength" : 63
    },
    "Device" : {
      "description" : "The Edge Device you want to register against a device fleet",
      "$ref" : "#/definitions/Device"
    },
    "Tags" : {
      "description" : "Associate tags with the resource",
      "type" : "array",
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    }
  },
  "required" : [ "DeviceFleetName" ],
  "additionalProperties" : False,
  "primaryIdentifier" : [ "/properties/Device/DeviceName" ],
  "createOnlyProperties" : [ "/properties/Device/DeviceName" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "sagemaker:RegisterDevices" ]
    },
    "read" : {
      "permissions" : [ "sagemaker:DescribeDevice" ]
    },
    "update" : {
      "permissions" : [ "sagemaker:UpdateDevices" ]
    },
    "delete" : {
      "permissions" : [ "sagemaker:DeregisterDevices" ]
    }
  }
}