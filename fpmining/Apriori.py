<?php
/**
 * @link http://www.yiiframework.com/
 * @copyright Copyright (c) 2008 Yii Software LLC
 * @license http://www.yiiframework.com/license/
 */

namespace yii\console\controllers;

use Yii;
use yii\base\Application;
use yii\console\Controller;
use yii\console\Exception;
use yii\helpers\Console;
use yii\helpers\Inflector;

/**
 * Provides help information about console commands.
 *
 * This command displays the available command list in
 * the application or the detailed instructions about using
 * a specific command.
 *
 * This command can be used as follows on command line:
 *
 * ```
 * yii help [command name]
 * ```
 *
 * In the above, if the command name is not provided, all
 * available commands will be displayed.
 *
 * @property array $commands All available command names. This property is read-only.
 *
 * @author Qiang Xue <qiang.xue@gmail.com>
 * @since 2.0
 */
class HelpController extends Controller
{
    /**
     * Displays available commands or the detailed information
     * about a particular command.
     *
     * @param string $command The name of the command to show help about.
     * If not provided, all available commands will be displayed.
     * @return integer the exit status
     * @throws Exception if the command for help is unknown
     */
    public function actionIndex($command = null)
    {
        if ($command !== null) {
            $result = Yii::$app->createController($command);
            if ($result === false) {
                $name = $this->ansiFormat($command, Console::FG_YELLOW);
                throw new Exception("No help for unknown command \"$name\".");
            }

            list($controller, $actionID) = $result;

            $actions = $this->getActions($controller);
            if ($actionID !== '' || count($actions) === 1 && $actions[0] === $controller->defaultAction) {
                $this->getSubCommandHelp($controller, $actionID);
            } else {
                $this->getCommandHelp($controller);
            }
        } else {
            $this->getDefaultHelp();
        }
    }

    /**
     * Returns all available command names.
     * @return array all available command names
     */
    public function getCommands()
    {
        $commands = $this->getModuleCommands(Yii::$app);
        sort($commands);
        return array_unique($commands);
    }

    /**
     * Returns an array of commands an their descriptions.
     * @return array all available commands as keys and their description as values.
     */
    protected function getCommandDe