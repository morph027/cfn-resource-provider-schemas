SCHEMA = {
  "typeName" : "AWS::IoTEvents::AlarmModel",
  "description" : "Represents an alarm model to monitor an ITE input attribute. You can use the alarm to get notified when the value is outside a specified range. For more information, see [Create an alarm model](https://docs.aws.amazon.com/iotevents/latest/developerguide/create-alarms.html) in the *Developer Guide*.",
  "sourceUrl" : "https://github.com/aws-cloudformation/aws-cloudformation-rpdk.git",
  "definitions" : {
    "AlarmRule" : {
      "type" : "object",
      "description" : "Defines when your alarm is invoked.",
      "additionalProperties" : False,
      "properties" : {
        "SimpleRule" : {
          "$ref" : "#/definitions/SimpleRule",
          "description" : "A rule that compares an input property value to a threshold value with a comparison operator."
        }
      }
    },
    "SimpleRule" : {
      "type" : "object",
      "additionalProperties" : False,
      "description" : "A rule that compares an input property value to a threshold value with a comparison operator.",
      "properties" : {
        "InputProperty" : {
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 512,
          "description" : "The value on the left side of the comparison operator. You can specify an ITE input attribute as an input property."
        },
        "ComparisonOperator" : {
          "type" : "string",
          "enum" : [ "GREATER", "GREATER_OR_EQUAL", "LESS", "LESS_OR_EQUAL", "EQUAL", "NOT_EQUAL" ],
          "description" : "The comparison operator."
        },
        "Threshold" : {
          "type" : "string",
          "minLength" : 1,
          "maxLength" : 512,
          "description" : "The value on the right side of the comparison operator. You can enter a number or specify an ITE input attribute."
        }
      },
      "required" : [ "InputProperty", "ComparisonOperator", "Threshold" ]
    },
    "AlarmEventActions" : {
      "type" : "object",
      "additionalProperties" : False,
      "description" : "Contains information about one or more alarm actions.",
      "properties" : {
        "AlarmActions" : {
          "$ref" : "#/definitions/AlarmActions",
          "description" : "Specifies one or more supported actions to receive notifications when the alarm state changes."
        }
      }
    },
    "AlarmCapabilities" : {
      "type" : "object",
      "description" : "Contains the configuration information of alarm state changes.",
      "additionalProperties" : False,
      "properties" : {
        "InitializationConfiguration" : {
          "$ref" : "#/definitions/InitializationConfiguration",
          "description" : "Specifies the default alarm state. The configuration applies to all alarms that were created based on this alarm model."
        },
        "AcknowledgeFlow" : {
          "$ref" : "#/definitions/AcknowledgeFlow",
          "description" : "Specifies whether to get notified for alarm state changes."
        }
      }
    },
    "AlarmActions" : {
      "type" : "array",
      "description" : "Specifies one or more supported actions to receive notifications when the alarm state changes.",
      "uniqueItems" : False,
      "insertionOrder" : False,
      "items" : {
        "$ref" : "#/definitions/AlarmAction"
      }
    },
    "AlarmAction" : {
      "type" : "object",
      "additionalProperties" : False,
      "description" : "Specifies one of the following actions to receive notifications when the alarm state changes.",
      "properties" : {
        "DynamoDB" : {
          "$ref" : "#/definitions/DynamoDB",
          "description" : "Defines an action to write to the Amazon DynamoDB table that you created. The standard action payload contains all the information about the detector model instance and the event that triggered the action. You can customize the [payload](https://docs.aws.amazon.com/iotevents/latest/apireference/API_Payload.html). One column of the DynamoDB table receives all attribute-value pairs in the payload that you specify.\n You must use expressions for all parameters in ``DynamoDBAction``. The expressions accept literals, operators, functions, references, and substitution templates.\n  **Examples**\n +  For literal values, the expressions must contain single quotes. For example, the value for the ``hashKeyType`` parameter can be ``'STRING'``.\n  +  For references, you must specify either variables or input values. For example, the value for the ``hashKeyField`` parameter can be ``$input.GreenhouseInput.name``.\n  +  For a substitution template, you must use ``${}``, and the template must be in single quotes. A substitution template can also contain a combination of literals, operators, functions, references, and substitution templates.\n In the following example, the value for the ``hashKeyValue`` parameter uses a substitution template. \n  ``'${$input.GreenhouseInput.temperature * 6 / 5 + 32} in Fahrenheit'`` \n  +  For a string concatenation, you must use ``+``. A string concatenation can also contain a combination of literals, operators, functions, references, and substitution templates.\n In the following example, the value for the ``tableName`` parameter uses a string concatenation. \n  ``'GreenhouseTemperatureTable ' + $input.GreenhouseInput.date`` \n  \n For more information, see [Expressions](https://docs.aws.amazon.com/iotevents/latest/developerguide/iotevents-expressions.html) in the *Developer Guide*.\n If the defined payload type is a string, ``DynamoDBAction`` writes non-JSON data to the DynamoDB table as binary data. The DynamoDB console displays the data as Base64-encoded text. The value for the ``payloadField`` parameter is ``<payload-field>_raw``."
        },
        "DynamoDBv2" : {
          "$ref" : "#/definitions/DynamoDBv2",
          "description" : "Defines an action to write to the Amazon DynamoDB table that you created. The default action payload contains all the information about the detector model instance and the event that triggered the action. You can customize the [payload](https://docs.aws.amazon.com/iotevents/latest/apireference/API_Payload.html). A separate column of the DynamoDB table receives one attribute-value pair in the payload that you specify.\n You must use expressions for all parameters in ``DynamoDBv2Action``. The expressions accept literals, operators, functions, references, and substitution templates.\n  **Examples**\n +  For literal values, the expressions must contain single quotes. For example, the value for the ``tableName`` parameter can be ``'GreenhouseTemperatureTable'``.\n  +  For references, you must specify either variables or input values. For example, the value for the ``tableName`` parameter can be ``$variable.ddbtableName``.\n  +  For a substitution template, you must use ``${}``, and the template must be in single quotes. A substitution template can also contain a combination of literals, operators, functions, references, and substitution templates.\n In the following example, the value for the ``contentExpression`` parameter in ``Payload`` uses a substitution template. \n  ``'{\\\"sensorID\\\": \\\"${$input.GreenhouseInput.sensor_id}\\\", \\\"temperature\\\": \\\"${$input.GreenhouseInput.temperature * 9 / 5 + 32}\\\"}'`` \n  +  For a string concatenation, you must use ``+``. A string concatenation can also contain a combination of literals, operators, functions, references, and substitution templates.\n In the following example, the value for the ``tableName`` parameter uses a string concatenation. \n  ``'GreenhouseTemperatureTable ' + $input.GreenhouseInput.date`` \n  \n For more information, see [Expressions](https://docs.aws.amazon.com/iotevents/latest/developerguide/iotevents-expressions.html) in the *Developer Guide*.\n The value for the ``type`` parameter in ``Payload`` must be ``JSON``."
        },
        "Firehose" : {
          "$ref" : "#/definitions/Firehose",
          "description" : "Sends information about the detector model instance and the event that triggered the action to an Amazon Kinesis Data Firehose delivery stream."
        },
        "IotEvents" : {
          "$ref" : "#/definitions/IotEvents",
          "description" : "Sends an ITE input, passing in information about the detector model instance and the event that triggered the action."
        },
        "IotSiteWise" : {
          "$ref" : "#/definitions/IotSiteWise",
          "description" : "Sends information about the detector model instance and the event that triggered the action to a specified asset property in ITSW.\n You must use expressions for all parameters in ``IotSiteWiseAction``. The expressions accept literals, operators, functions, references, and substitutions templates.\n  **Examples**\n +  For literal values, the expressions must contain single quotes. For example, the value for the ``propertyAlias`` parameter can be ``'/company/windfarm/3/turbine/7/temperature'``.\n  +  For references, you must specify either variables or input values. For example, the value for the ``assetId`` parameter can be ``$input.TurbineInput.assetId1``.\n  +  For a substitution template, you must use ``${}``, and the template must be in single quotes. A substitution template can also contain a combination of literals, operators, functions, references, and substitution templates.\n In the following example, the value for the ``propertyAlias`` parameter uses a substitution template. \n  ``'company/windfarm/${$input.TemperatureInput.sensorData.windfarmID}/turbine/ ${$input.TemperatureInput.sensorData.turbineID}/temperature'`` \n  \n You must specify either ``propertyAlias`` or both ``assetId`` and ``propertyId`` to identify the target asset property in ITSW.\n For more information, see [Expressions](https://docs.aws.amazon.com/iotevents/latest/developerguide/iotevents-expressions.html) in the *Developer Guide*."
        },
        "IotTopicPublish" : {
          "$ref" : "#/definitions/IotTopicPublish",
          "description" : "Information required to publish the MQTT message through the IoT message broker."
        },
        "Lambda" : {
          "$ref" : "#/definitions/Lambda",
          "description" : "Calls a Lambda function, passing in information about the detector model instance and the event that triggered the action."
        },
        "Sns" : {
          "$ref" : "#/definitions/Sns",
          "description" : "Information required to publish the Amazon SNS message."
        },
        "Sqs" : {
          "$ref" : "#/definitions/Sqs",
          "description" : "Sends information about the detector model instance and the event that triggered the action to an Amazon SQS queue."
        }
      }
    },
    "DynamoDB" : {
      "type" : "object",
      "additionalProperties" : False,
      "description" : "Defines an action to write to the Amazon DynamoDB table that you created. The standard action payload contains all the information about the detector model instance and the event that triggered the action. You can customize the [payload](https://docs.aws.amazon.com/iotevents/latest/apireference/API_Payload.html). One column of the DynamoDB table receives all attribute-value pairs in the payload that you specify.\n You must use expressions for all parameters in ``DynamoDBAction``. The expressions accept literals, operators, functions, references, and substitution templates.\n  **Examples**\n +  For literal values, the expressions must contain single quotes. For example, the value for the ``hashKeyType`` parameter can be ``'STRING'``.\n  +  For references, you must specify either variables or input values. For example, the value for the ``hashKeyField`` parameter can be ``$input.GreenhouseInput.name``.\n  +  For a substitution template, you must use ``${}``, and the template must be in single quotes. A substitution template can also contain a combination of literals, operators, functions, references, and substitution templates.\n In the following example, the value for the ``hashKeyValue`` parameter uses a substitution template. \n  ``'${$input.GreenhouseInput.temperature * 6 / 5 + 32} in Fahrenheit'`` \n  +  For a string concatenation, you must use ``+``. A string concatenation can also contain a combination of literals, operators, functions, references, and substitution templates.\n In the following example, the value for the ``tableName`` parameter uses a string concatenation. \n  ``'GreenhouseTemperatureTable ' + $input.GreenhouseInput.date`` \n  \n For more information, see [Expressions](https://docs.aws.amazon.com/iotevents/latest/developerguide/iotevents-expressions.html) in the *Developer Guide*.\n If the defined payload type is a string, ``DynamoDBAction`` writes non-JSON data to the DynamoDB table as binary data. The DynamoDB console displays the data as Base64-encoded text. The value for the ``payloadField`` parameter is ``<payload-field>_raw``.",
      "properties" : {
        "HashKeyField" : {
          "type" : "string",
          "description" : "The name of the hash key (also called the partition key). The ``hashKeyField`` value must match the partition key of the target DynamoDB table."
        },
        "HashKeyType" : {
          "type" : "string",
          "description" : "The data type for the hash key (also called the partition key). You can specify the following values:\n  +   ``'STRING'`` - The hash key is a string.\n  +   ``'NUMBER'`` - The hash key is a number.\n  \n If you don't specify ``hashKeyType``, the default value is ``'STRING'``."
        },
        "HashKeyValue" : {
          "type" : "string",
          "description" : "The value of the hash key (also called the partition key)."
        },
        "Operation" : {
          "type" : "string",
          "description" : "The type of operation to perform. You can specify the following values: \n  +   ``'INSERT'`` - Insert data as a new item into the DynamoDB table. This item uses the specified hash key as a partition key. If you specified a range key, the item uses the range key as a sort key.\n  +   ``'UPDATE'`` - Update an existing item of the DynamoDB table with new data. This item's partition key must match the specified hash key. If you specified a range key, the range key must match the item's sort key.\n  +   ``'DELETE'`` - Delete an existing item of the DynamoDB table. This item's partition key must match the specified hash key. If you specified a range key, the range key must match the item's sort key.\n  \n If you don't specify this parameter, ITE triggers the ``'INSERT'`` operation."
        },
        "Payload" : {
          "$ref" : "#/definitions/Payload",
          "description" : "Information needed to configure the payload.\n By default, ITE generates a standard payload in JSON for any action. This action payload contains all attribute-value pairs that have the information about the detector model instance and the event triggered the action. To configure the action payload, you can use ``contentExpression``."
        },
        "PayloadField" : {
          "type" : "string",
          "description" : "The name of the DynamoDB column that receives the action payload.\n If you don't specify this parameter, the name of the DynamoDB column is ``payload``."
        },
        "RangeKeyField" : {
          "type" : "string",
          "description" : "The name of the range key (also called the sort key). The ``rangeKeyField`` value must match the sort key of the target DynamoDB table."
        },
        "RangeKeyType" : {
          "type" : "string",
          "description" : "The data type for the range key (also called the sort key), You can specify the following values:\n  +   ``'STRING'`` - The range key is a string.\n  +   ``'NUMBER'`` - The range key is number.\n  \n If you don't specify ``rangeKeyField``, the default value is ``'STRING'``."
        },
        "RangeKeyValue" : {
          "type" : "string",
          "description" : "The value of the range key (also called the sort key)."
        },
        "TableName" : {
          "type" : "string",
          "description" : "The name of the DynamoDB table. The ``tableName`` value must match the table name of the target DynamoDB table."
        }
      },
      "required" : [ "HashKeyField", "HashKeyValue", "TableName" ]
    },
    "DynamoDBv2" : {
      "type" : "object",
      "additionalProperties" : False,
      "description" : "Defines an action to write to the Amazon DynamoDB table that you created. The default action payload contains all the information about the detector model instance and the event that triggered the action. You can customize the [payload](https://docs.aws.amazon.com/iotevents/latest/apireference/API_Payload.html). A separate column of the DynamoDB table receives one attribute-value pair in the payload that you specify.\n You must use expressions for all parameters in ``DynamoDBv2Action``. The expressions accept literals, operators, functions, references, and substitution templates.\n  **Examples**\n +  For literal values, the expressions must contain single quotes. For example, the value for the ``tableName`` parameter can be ``'GreenhouseTemperatureTable'``.\n  +  For references, you must specify either variables or input values. For example, the value for the ``tableName`` parameter can be ``$variable.ddbtableName``.\n  +  For a substitution template, you must use ``${}``, and the template must be in single quotes. A substitution template can also contain a combination of literals, operators, functions, references, and substitution templates.\n In the following example, the value for the ``contentExpression`` parameter in ``Payload`` uses a substitution template. \n  ``'{\\\"sensorID\\\": \\\"${$input.GreenhouseInput.sensor_id}\\\", \\\"temperature\\\": \\\"${$input.GreenhouseInput.temperature * 9 / 5 + 32}\\\"}'`` \n  +  For a string concatenation, you must use ``+``. A string concatenation can also contain a combination of literals, operators, functions, references, and substitution templates.\n In the following example, the value for the ``tableName`` parameter uses a string concatenation. \n  ``'GreenhouseTemperatureTable ' + $input.GreenhouseInput.date`` \n  \n For more information, see [Expressions](https://docs.aws.amazon.com/iotevents/latest/developerguide/iotevents-expressions.html) in the *Developer Guide*.\n The value for the ``type`` parameter in ``Payload`` must be ``JSON``.",
      "properties" : {
        "Payload" : {
          "$ref" : "#/definitions/Payload",
          "description" : "Information needed to configure the payload.\n By default, ITE generates a standard payload in JSON for any action. This action payload contains all attribute-value pairs that have the information about the detector model instance and the event triggered the action. To configure the action payload, you can use ``contentExpression``."
        },
        "TableName" : {
          "type" : "string",
          "description" : "The name of the DynamoDB table."
        }
      },
      "required" : [ "TableName" ]
    },
    "Firehose" : {
      "type" : "object",
      "additionalProperties" : False,
      "description" : "Sends information about the detector model instance and the event that triggered the action to an Amazon Kinesis Data Firehose delivery stream.",
      "properties" : {
        "DeliveryStreamName" : {
          "type" : "string",
          "description" : "The name of the Kinesis Data Firehose delivery stream where the data is written."
        },
        "Payload" : {
          "$ref" : "#/definitions/Payload",
          "description" : "You can configure the action payload when you send a message to an Amazon Data Firehose delivery stream."
        },
        "Separator" : {
          "type" : "string",
          "description" : "A character separator that is used to separate records written to the Kinesis Data Firehose delivery stream. Valid values are: '\\n' (newline), '\\t' (tab), '\\r\\n' (Windows newline), ',' (comma).",
          "pattern" : "([\\n\\t])|(\\r\\n)|(,)"
        }
      },
      "required" : [ "DeliveryStreamName" ]
    },
    "IotEvents" : {
      "type" : "object",
      "additionalProperties" : False,
      "description" : "Sends an ITE input, passing in information about the detector model instance and the event that triggered the action.",
      "properties" : {
        "InputName" : {
          "type" : "string",
          "description" : "The name of the ITE input where the data is sent.",
          "minLength" : 1,
          "maxLength" : 128,
          "pattern" : "^[a-zA-Z][a-zA-Z0-9_]*$"
        },
        "Payload" : {
          "$ref" : "#/definitions/Payload",
          "description" : "You can configure the action payload when you send a message to an ITE input."
        }
      },
      "required" : [ "InputName" ]
    },
    "IotSiteWise" : {
      "type" : "object",
      "additionalProperties" : False,
      "description" : "Sends information about the detector model instance and the event that triggered the action to a specified asset property in ITSW.\n You must use expressions for all parameters in ``IotSiteWiseAction``. The expressions accept literals, operators, functions, references, and substitutions templates.\n  **Examples**\n +  For literal values, the expressions must contain single quotes. For example, the value for the ``propertyAlias`` parameter can be ``'/company/windfarm/3/turbine/7/temperature'``.\n  +  For references, you must specify either variables or input values. For example, the value for the ``assetId`` parameter can be ``$input.TurbineInput.assetId1``.\n  +  For a substitution template, you must use ``${}``, and the template must be in single quotes. A substitution template can also contain a combination of literals, operators, functions, references, and substitution templates.\n In the following example, the value for the ``propertyAlias`` parameter uses a substitution template. \n  ``'company/windfarm/${$input.TemperatureInput.sensorData.windfarmID}/turbine/ ${$input.TemperatureInput.sensorData.turbineID}/temperature'`` \n  \n You must specify either ``propertyAlias`` or both ``assetId`` and ``propertyId`` to identify the target asset property in ITSW.\n For more information, see [Expressions](https://docs.aws.amazon.com/iotevents/latest/developerguide/iotevents-expressions.html) in the *Developer Guide*.",
      "properties" : {
        "AssetId" : {
          "type" : "string",
          "description" : "The ID of the asset that has the specified property."
        },
        "EntryId" : {
          "type" : "string",
          "description" : "A unique identifier for this entry. You can use the entry ID to track which data entry causes an error in case of failure. The default is a new unique identifier."
        },
        "PropertyAlias" : {
          "type" : "string",
          "description" : "The alias of the asset property."
        },
        "PropertyId" : {
          "type" : "string",
          "description" : "The ID of the asset property."
        },
        "PropertyValue" : {
          "$ref" : "#/definitions/AssetPropertyValue",
          "description" : "The value to send to the asset property. This value contains timestamp, quality, and value (TQV) information."
        }
      }
    },
    "IotTopicPublish" : {
      "type" : "object",
      "additionalProperties" : False,
      "description" : "Information required to publish the MQTT message through the IoT message broker.",
      "properties" : {
        "MqttTopic" : {
          "type" : "string",
          "description" : "The MQTT topic of the message. You can use a string expression that includes variables (``$variable.<variable-name>``) and input values (``$input.<input-name>.<path-to-datum>``) as the topic string.",
          "minLength" : 1,
          "maxLength" : 128
        },
        "Payload" : {
          "$ref" : "#/definitions/Payload",
          "description" : "You can configure the action payload when you publish a message to an IoTCore topic."
        }
      },
      "required" : [ "MqttTopic" ]
    },
    "Lambda" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "FunctionArn" : {
          "type" : "string",
          "description" : "The ARN of the Lambda function that is executed.",
          "minLength" : 1,
          "maxLength" : 2048
        },
        "Payload" : {
          "$ref" : "#/definitions/Payload",
          "description" : "You can configure the action payload when you send a message to a Lambda function."
        }
      },
      "required" : [ "FunctionArn" ],
      "description" : "Calls a Lambda function, passing in information about the detector model instance and the event that triggered the action."
    },
    "Sns" : {
      "type" : "object",
      "additionalProperties" : False,
      "description" : "Information required to publish the Amazon SNS message.",
      "properties" : {
        "Payload" : {
          "$ref" : "#/definitions/Payload",
          "description" : "You can configure the action payload when you send a message as an Amazon SNS push notification."
        },
        "TargetArn" : {
          "type" : "string",
          "description" : "The ARN of the Amazon SNS target where the message is sent.",
          "minLength" : 1,
          "maxLength" : 2048
        }
      },
      "required" : [ "TargetArn" ]
    },
    "Sqs" : {
      "type" : "object",
      "additionalProperties" : False,
      "properties" : {
        "Payload" : {
          "$ref" : "#/definitions/Payload",
          "description" : "You can configure the action payload when you send a message to an Amazon SQS queue."
        },
        "QueueUrl" : {
          "type" : "string",
          "description" : "The URL of the SQS queue where the data is written."
        },
        "UseBase64" : {
          "type" : "boolean",
          "description" : "Set this to TRUE if you want the data to be base-64 encoded before it is written to the queue. Otherwise, set this to FALSE."
        }
      },
      "required" : [ "QueueUrl" ],
      "description" : "Sends information about the detector model instance and the event that triggered the action to an Amazon SQS queue."
    },
    "Payload" : {
      "type" : "object",
      "additionalProperties" : False,
      "description" : "Information needed to configure the payload.\n By default, ITE generates a standard payload in JSON for any action. This action payload contains all attribute-value pairs that have the information about the detector model instance and the event triggered the action. To configure the action payload, you can use ``contentExpression``.",
      "properties" : {
        "ContentExpression" : {
          "type" : "string",
          "description" : "The content of the payload. You can use a string expression that includes quoted strings (``'<string>'``), variables (``$variable.<variable-name>``), input values (``$input.<input-name>.<path-to-datum>``), string concatenations, and quoted strings that contain ``${}`` as the content. The recommended maximum size of a content expression is 1 KB.",
          "minLength" : 1
        },
        "Type" : {
          "type" : "string",
          "description" : "The value of the payload type can be either ``STRING`` or ``JSON``."
        }
      },
      "required" : [ "ContentExpression", "Type" ]
    },
    "InitializationConfiguration" : {
      "type" : "object",
      "description" : "Specifies the default alarm state. The configuration applies to all alarms that were created based on this alarm model.",
      "additionalProperties" : False,
      "properties" : {
        "DisabledOnInitialization" : {
          "type" : "boolean",
          "description" : "The value must be ``TRUE`` or ``FALSE``. If ``FALSE``, all alarm instances created based on the alarm model are activated. The default value is ``TRUE``.",
          "default" : "True"
        }
      },
      "required" : [ "DisabledOnInitialization" ]
    },
    "AcknowledgeFlow" : {
      "type" : "object",
      "description" : "Specifies whether to get notified for alarm state changes.",
      "additionalProperties" : False,
      "properties" : {
        "Enabled" : {
          "type" : "boolean",
          "description" : "The value must be ``TRUE`` or ``FALSE``. If ``TRUE``, you receive a notification when the alarm state changes. You must choose to acknowledge the notification before the alarm state can return to ``NORMAL``. If ``FALSE``, you won't receive notifications. The alarm automatically changes to the ``NORMAL`` state when the input property value returns to the specified range.",
          "default" : "True"
        }
      }
    },
    "AssetPropertyValue" : {
      "type" : "object",
      "additionalProperties" : False,
      "description" : "A structure that contains value information. For more information, see [AssetPropertyValue](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_AssetPropertyValue.html) in the *API Reference*.\n You must use expressions for all parameters in ``AssetPropertyValue``. The expressions accept literals, operators, functions, references, and substitution templates.\n  **Examples**\n +  For literal values, the expressions must contain single quotes. For example, the value for the ``quality`` parameter can be ``'GOOD'``.\n  +  For references, you must specify either variables or input values. For example, the value for the ``quality`` parameter can be ``$input.TemperatureInput.sensorData.quality``.\n  \n For more information, see [Expressions](https://docs.aws.amazon.com/iotevents/latest/developerguide/iotevents-expressions.html) in the *Developer Guide*.",
      "properties" : {
        "Quality" : {
          "type" : "string",
          "description" : "The quality of the asset property value. The value must be ``'GOOD'``, ``'BAD'``, or ``'UNCERTAIN'``."
        },
        "Timestamp" : {
          "$ref" : "#/definitions/AssetPropertyTimestamp",
          "description" : "The timestamp associated with the asset property value. The default is the current event time."
        },
        "Value" : {
          "$ref" : "#/definitions/AssetPropertyVariant",
          "description" : "The value to send to an asset property."
        }
      },
      "required" : [ "Value" ]
    },
    "AssetPropertyTimestamp" : {
      "type" : "object",
      "additionalProperties" : False,
      "description" : "A structure that contains timestamp information. For more information, see [TimeInNanos](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_TimeInNanos.html) in the *API Reference*.\n You must use expressions for all parameters in ``AssetPropertyTimestamp``. The expressions accept literals, operators, functions, references, and substitution templates.\n  **Examples**\n +  For literal values, the expressions must contain single quotes. For example, the value for the ``timeInSeconds`` parameter can be ``'1586400675'``.\n  +  For references, you must specify either variables or input values. For example, the value for the ``offsetInNanos`` parameter can be ``$variable.time``.\n  +  For a substitution template, you must use ``${}``, and the template must be in single quotes. A substitution template can also contain a combination of literals, operators, functions, references, and substitution templates.\n In the following example, the value for the ``timeInSeconds`` parameter uses a substitution template.\n  ``'${$input.TemperatureInput.sensorData.timestamp / 1000}'`` \n  \n For more information, see [Expressions](https://docs.aws.amazon.com/iotevents/latest/developerguide/iotevents-expressions.html) in the *Developer Guide*.",
      "properties" : {
        "OffsetInNanos" : {
          "type" : "string",
          "description" : "The nanosecond offset converted from ``timeInSeconds``. The valid range is between 0-999999999."
        },
        "TimeInSeconds" : {
          "type" : "string",
          "description" : "The timestamp, in seconds, in the Unix epoch format. The valid range is between 1-31556889864403199."
        }
      },
      "required" : [ "TimeInSeconds" ]
    },
    "AssetPropertyVariant" : {
      "type" : "object",
      "additionalProperties" : False,
      "description" : "A structure that contains an asset property value. For more information, see [Variant](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_Variant.html) in the *API Reference*.\n You must use expressions for all parameters in ``AssetPropertyVariant``. The expressions accept literals, operators, functions, references, and substitution templates.\n  **Examples**\n +  For literal values, the expressions must contain single quotes. For example, the value for the ``integerValue`` parameter can be ``'100'``.\n  +  For references, you must specify either variables or parameters. For example, the value for the ``booleanValue`` parameter can be ``$variable.offline``.\n  +  For a substitution template, you must use ``${}``, and the template must be in single quotes. A substitution template can also contain a combination of literals, operators, functions, references, and substitution templates. \n In the following example, the value for the ``doubleValue`` parameter uses a substitution template. \n  ``'${$input.TemperatureInput.sensorData.temperature * 6 / 5 + 32}'`` \n  \n For more information, see [Expressions](https://docs.aws.amazon.com/iotevents/latest/developerguide/iotevents-expressions.html) in the *Developer Guide*.\n You must specify one of the following value types, depending on the ``dataType`` of the specified asset property. For more information, see [AssetProperty](https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_AssetProperty.html) in the *API Reference*.",
      "properties" : {
        "BooleanValue" : {
          "type" : "string",
          "description" : "The asset property value is a Boolean value that must be ``'TRUE'`` or ``'FALSE'``. You must use an expression, and the evaluated result should be a Boolean value."
        },
        "DoubleValue" : {
          "type" : "string",
          "description" : "The asset property value is a double. You must use an expression, and the evaluated result should be a double."
        },
        "IntegerValue" : {
          "type" : "string",
          "description" : "The asset property value is an integer. You must use an expression, and the evaluated result should be an integer."
        },
        "StringValue" : {
          "type" : "string",
          "description" : "The asset property value is a string. You must use an expression, and the evaluated result should be a string."
        }
      }
    },
    "Tag" : {
      "type" : "object",
      "additionalProperties" : False,
      "description" : "Metadata that can be used to manage the resource.",
      "properties" : {
        "Key" : {
          "description" : "The tag's key.",
          "type" : "string"
        },
        "Value" : {
          "description" : "The tag's value.",
          "type" : "string"
        }
      },
      "required" : [ "Value", "Key" ]
    }
  },
  "properties" : {
    "AlarmModelName" : {
      "type" : "string",
      "description" : "The name of the alarm model.",
      "minLength" : 1,
      "maxLength" : 128,
      "pattern" : "^[a-zA-Z0-9_-]+$"
    },
    "AlarmModelDescription" : {
      "type" : "string",
      "description" : "The description of the alarm model.",
      "maxLength" : 1024
    },
    "RoleArn" : {
      "type" : "string",
      "description" : "The ARN of the IAM role that allows the alarm to perform actions and access AWS resources. For more information, see [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) in the *General Reference*.",
      "minLength" : 1,
      "maxLength" : 2048
    },
    "Key" : {
      "type" : "string",
      "description" : "An input attribute used as a key to create an alarm. ITE routes [inputs](https://docs.aws.amazon.com/iotevents/latest/apireference/API_Input.html) associated with this key to the alarm.",
      "minLength" : 1,
      "maxLength" : 128,
      "pattern" : "^((`[\\w\\- ]+`)|([\\w\\-]+))(\\.((`[\\w\\- ]+`)|([\\w\\-]+)))*$"
    },
    "Severity" : {
      "type" : "integer",
      "description" : "A non-negative integer that reflects the severity level of the alarm.",
      "minimum" : 0,
      "maximum" : 2147483647
    },
    "AlarmRule" : {
      "$ref" : "#/definitions/AlarmRule",
      "description" : "Defines when your alarm is invoked."
    },
    "AlarmEventActions" : {
      "$ref" : "#/definitions/AlarmEventActions",
      "description" : "Contains information about one or more alarm actions."
    },
    "AlarmCapabilities" : {
      "$ref" : "#/definitions/AlarmCapabilities",
      "description" : "Contains the configuration information of alarm state changes."
    },
    "Tags" : {
      "type" : "array",
      "uniqueItems" : False,
      "insertionOrder" : False,
      "description" : "A list of key-value pairs that contain metadata for the alarm model. The tags help you manage the alarm model. For more information, see [Tagging your resources](https://docs.aws.amazon.com/iotevents/latest/developerguide/tagging-iotevents.html) in the *Developer Guide*.\n You can create up to 50 tags for one alarm model.",
      "items" : {
        "$ref" : "#/definitions/Tag"
      }
    }
  },
  "required" : [ "RoleArn", "AlarmRule" ],
  "additionalProperties" : False,
  "primaryIdentifier" : [ "/properties/AlarmModelName" ],
  "createOnlyProperties" : [ "/properties/AlarmModelName", "/properties/Key" ],
  "handlers" : {
    "create" : {
      "permissions" : [ "iotevents:CreateAlarmModel", "iotevents:UpdateInputRouting", "iotevents:DescribeAlarmModel", "iotevents:ListTagsForResource", "iotevents:TagResource", "iam:PassRole" ]
    },
    "read" : {
      "permissions" : [ "iotevents:DescribeAlarmModel", "iotevents:ListTagsForResource" ]
    },
    "update" : {
      "permissions" : [ "iotevents:UpdateAlarmModel", "iotevents:UpdateInputRouting", "iotevents:DescribeAlarmModel", "iotevents:ListTagsForResource", "iotevents:UntagResource", "iotevents:TagResource", "iam:PassRole" ]
    },
    "delete" : {
      "permissions" : [ "iotevents:DeleteAlarmModel", "iotevents:DescribeAlarmModel" ]
    },
    "list" : {
      "permissions" : [ "iotevents:ListAlarmModels" ]
    }
  },
  "tagging" : {
    "taggable" : True,
    "tagOnCreate" : True,
    "tagUpdatable" : True,
    "cloudFormationSystemTags" : False,
    "tagProperty" : "/properties/Tags",
    "permissions" : [ "iotevents:UntagResource", "iotevents:TagResource", "iotevents:ListTagsForResource" ]
  }
}